"""Read-only static checks; no skill execution, browser, or network requests.

Link checks cover inline Markdown links and HTML fragments used by this package.
They are not a full Markdown parser, external URL checker, or security audit.
"""
import re
import unittest
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / 'skills' / 'native-operator-interaction'


class Markup(HTMLParser):
    def __init__(self):
        super().__init__()
        self.tags = []
        self.ids = []

    def handle_starttag(self, tag, attrs):
        attrs = dict(attrs)
        self.tags.append((tag, attrs))
        if 'id' in attrs:
            self.ids.append(attrs['id'])


class PackageChecks(unittest.TestCase):
    def test_metadata_and_small_core(self):
        text = (SKILL / 'SKILL.md').read_text(encoding='utf-8')
        self.assertTrue(text.startswith('---\n'))
        frontmatter = text.split('---\n', 2)[1]
        self.assertIn('name: native-operator-interaction', frontmatter)
        self.assertIn('description:', frontmatter)
        self.assertIn('license: MIT', frontmatter)
        self.assertIn('version: "0.2.0"', frontmatter)
        self.assertNotIn('candidate', frontmatter)
        self.assertLess(len(text.splitlines()), 500)

    def test_license_preserved_in_skill(self):
        root_license = (ROOT / 'LICENSE').read_bytes()
        self.assertEqual(root_license, (SKILL / 'LICENSE').read_bytes())
        text = root_license.decode('utf-8')
        self.assertTrue(text.startswith('MIT License\n'))
        self.assertIn('Copyright (c) 2026 Schatztruhe contributors', text)
        self.assertIn('Permission is hereby granted, free of charge', text)
        self.assertIn('THE SOFTWARE IS PROVIDED "AS IS"', text)

    def test_no_symlinks_or_unexpected_files(self):
        for path in SKILL.rglob('*'):
            self.assertFalse(path.is_symlink(), str(path))
            if path.is_file():
                self.assertTrue(path.name == 'LICENSE' or path.suffix in
                                {'.md', '.html', '.yaml', '.svg'}, str(path))

    def test_public_package_boundaries(self):
        expected_top = {'.gitignore', 'README.md', 'README.ru.md', 'CHANGELOG.md',
                        'LICENSE', 'docs', 'skills', 'tests'}
        # A local Git database and ignored caches are not release contents.
        ignored_dirs = {'.git', '__pycache__', '.pytest_cache'}
        actual_top = {p.name for p in ROOT.iterdir()
                      if p.name not in ignored_dirs}
        self.assertEqual(actual_top, expected_top)
        for path in ROOT.rglob('*'):
            relative = path.relative_to(ROOT)
            if any(part in ignored_dirs for part in relative.parts):
                continue
            self.assertFalse(path.is_symlink(), str(relative))
            self.assertNotIn(path.name, {'local-skill-audit.md', '.env'})
            self.assertFalse(path.name.startswith('.env.'), str(relative))
            self.assertNotIn(path.suffix.lower(), {'.pem', '.key', '.p12', '.pfx', '.log'})
            if path.is_file():
                self.assertGreater(path.stat().st_size, 0, str(relative))
                self.assertTrue(path.name in {'LICENSE', '.gitignore'} or
                                path.suffix in {'.md', '.html', '.py', '.yaml', '.svg'},
                                str(relative))

    def check_links(self, paths, boundary):
        for path in paths:
            for target in re.findall(r'\]\(([^)]+)\)', path.read_text(encoding='utf-8')):
                with self.subTest(document=str(path.relative_to(ROOT)), target=target):
                    parsed = urlsplit(target)
                    if parsed.scheme:
                        self.assertIn(parsed.scheme, {'https', 'http'})
                        self.assertTrue(parsed.netloc, target)
                        continue  # Availability of external URLs is not tested.
                    self.assertFalse(parsed.netloc, target)
                    self.assertFalse(parsed.query, target)
                    local = unquote(parsed.path)
                    self.assertFalse(Path(local).is_absolute(), target)
                    linked = (path.parent / local).resolve() if local else path.resolve()
                    self.assertTrue(linked.is_relative_to(boundary.resolve()), target)
                    self.assertTrue(linked.exists(), f'{path}: {target}')
                    if parsed.fragment:
                        # The current Markdown links have no heading fragments.
                        # Explicitly reject unsupported fragment validation rather
                        # than silently claiming to have checked it.
                        self.assertEqual(linked.suffix, '.html', target)
                        parser = Markup()
                        parser.feed(linked.read_text(encoding='utf-8'))
                        self.assertIn(unquote(parsed.fragment), parser.ids)

    def test_skill_reference_links(self):
        self.check_links(SKILL.rglob('*.md'), SKILL)

    def test_public_document_local_links(self):
        self.check_links(list(ROOT.glob('*.md')) + list((ROOT / 'docs').rglob('*.md')), ROOT)

    def test_release_identity_in_overviews(self):
        target = 'https://github.com/Hanukashats/Schatztruhe/releases/tag/native-operator-interaction-v0.2.0'
        for name in ['README.md', 'README.ru.md']:
            text = (ROOT / name).read_text(encoding='utf-8')
            self.assertTrue(text.startswith('# Schatztruhe\n'))
            self.assertIn(target, text)
            self.assertIn('0.2.0', text)
            self.assertIn('MIT', text)
        for path in list(ROOT.glob('*.md')) + list((ROOT / 'docs').glob('*.md')):
            self.assertNotIn('0.2.0-candidate', path.read_text(encoding='utf-8'))

    def test_static_html_safety_and_structure(self):
        html = (SKILL / 'assets' / 'interactive-report.html').read_text(encoding='utf-8')
        parser = Markup()
        parser.feed(html)
        self.assertEqual(len(parser.ids), len(set(parser.ids)))
        self.assertIn(('html', {'lang': 'ru'}), parser.tags)
        self.assertEqual(sum(tag == 'h1' for tag, _ in parser.tags), 1)
        for tag, attrs in parser.tags:
            self.assertFalse(any(key.startswith('on') for key in attrs), tag)
            self.assertNotIn(tag, {'iframe', 'object', 'embed'})
            if tag in {'script', 'img', 'link', 'source'}:
                self.assertNotIn('src', attrs)
                self.assertFalse(attrs.get('href', '').startswith(('http:', 'https:', '//')))
            href = attrs.get('href', '')
            if href.startswith('#'):
                self.assertIn(href[1:], parser.ids)
            for name in ('aria-labelledby', 'aria-describedby'):
                for referenced_id in attrs.get(name, '').split():
                    self.assertIn(referenced_id, parser.ids)
        self.assertNotRegex(html, r'\b(?:fetch|eval)\s*\(|\.innerHTML\s*=|XMLHttpRequest|WebSocket|sendBeacon')
        self.assertIn("connect-src 'none'", html)
        self.assertIn('prefers-reduced-motion', html)
        self.assertIn('@media print', html)
        self.assertIn('не измерение системы', html)
        self.assertIn('Сообщение не отправлено', html)
        for required in ['checks', 'checks-number', 'model-result', 'model-limits', 'reset', 'question', 'message']:
            self.assertIn(required, parser.ids)
        labels = {attrs.get('for') for tag, attrs in parser.tags if tag == 'label'}
        self.assertTrue({'checks', 'checks-number', 'question', 'message'} <= labels)


if __name__ == '__main__':
    unittest.main()
