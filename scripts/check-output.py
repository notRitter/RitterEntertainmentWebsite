"""Check routes, assets, anchors, and search metadata in the static build."""

import argparse
import os
import sys
from html.parser import HTMLParser
from pathlib import Path
from urllib.parse import unquote, urljoin, urlsplit
from xml.etree import ElementTree


class Page(HTMLParser):
    def __init__(self, path):
        super().__init__(convert_charrefs=True)
        self.ids = set()
        self.references = []
        self.meta = {}
        self.canonical = None
        self.title = None
        self.title_open = False
        self.h1_count = 0
        self.errors = []
        self.feed(path.read_text(encoding="utf-8"))

    def handle_starttag(self, tag, values):
        attrs = dict(values)
        if anchor := attrs.get("id"):
            if anchor in self.ids:
                self.errors.append(f"Duplicate id: {anchor}")
            self.ids.add(anchor)
        if tag == "title":
            self.title_open = True
        if tag == "h1":
            self.h1_count += 1
        if tag == "meta":
            self.meta[attrs.get("name") or attrs.get("property")] = attrs.get("content")
        if tag == "link" and attrs.get("rel") == "canonical":
            self.canonical = attrs.get("href")
        elif tag in ("a", "link", "img", "script"):
            key = "href" if tag in ("a", "link") else "src"
            if attrs.get(key):
                self.references.append(attrs[key])
        if tag == "img" and "alt" not in attrs:
            self.errors.append(f'Missing image alt attribute: {attrs.get("src")}')

    def handle_endtag(self, tag):
        if tag == "title":
            self.title_open = False

    def handle_data(self, value):
        if self.title_open:
            self.title = (self.title or "") + value


def main():
    arguments = argparse.ArgumentParser()
    arguments.add_argument("--dir", default="dist")
    arguments.add_argument(
        "--origin", default=os.environ.get("PAGES_ORIGIN") or "https://www.ritterentertainment.com"
    )
    arguments.add_argument("--base", default=os.environ.get("PAGES_BASE") or "/")
    arguments.add_argument("--list-external", action="store_true")
    args = arguments.parse_args()
    base = "/" + args.base.strip("/") + "/" if args.base.strip("/") else "/"
    origin = args.origin.rstrip("/")
    root_url = origin + base
    root = Path(args.dir)
    errors = []
    external = set()
    pages = {}
    canonical_pages = set()
    for path in sorted(root.rglob("*.html")):
        relative = path.relative_to(root).as_posix()
        route = relative.removesuffix("index.html") if path.name == "index.html" else relative
        pages[urljoin(root_url, route)] = (relative, Page(path))

    def check_reference(value, source):
        target = urlsplit(urljoin(source, value))
        if target.scheme not in ("http", "https"):
            return
        if target.netloc != urlsplit(origin).netloc:
            external.add(value)
            return
        if urlsplit(value).netloc and target.path.startswith("/SpawnerDocs/"):
            external.add(value)
            return
        if not target.path.startswith(base):
            errors.append(f"{source}: URL outside deployment base: {value}")
            return
        relative = unquote(target.path[len(base):])
        file = root / relative
        if file.is_dir():
            file /= "index.html"
        if not file.is_file():
            errors.append(f"{source}: missing output for {value}")
        if file.suffix == ".html" and target.fragment:
            if file.is_file() and unquote(target.fragment) not in Page(file).ids:
                errors.append(f"{source}: missing anchor for {value}")

    preview = urlsplit(origin).hostname.endswith(".github.io")
    for url, (file, page) in pages.items():
        errors.extend(f"{file}: {error}" for error in page.errors)
        if not page.title or not page.canonical:
            errors.append(f"{file}: title or canonical URL missing")
        legacy = file == "emc/index.html"
        if not legacy:
            if page.canonical != url or page.meta.get("og:url") != url:
                errors.append(f"{file}: canonical or Open Graph URL should be {url}")
            for field in ("description", "og:title", "og:description", "og:image", "og:image:alt"):
                if not page.meta.get(field):
                    errors.append(f"{file}: missing {field}")
            if page.h1_count != 1:
                errors.append(f"{file}: expected one h1, got {page.h1_count}")
        if preview or legacy or file == "404.html":
            if "noindex" not in (page.meta.get("robots") or ""):
                errors.append(f"{file}: expected noindex")
        elif page.meta.get("robots"):
            errors.append(f"{file}: production page has unexpected robots metadata")
        if not legacy and file != "404.html":
            canonical_pages.add(url)
        for value in [*page.references, page.canonical, page.meta.get("og:image")]:
            if value:
                check_reference(value, url)

    for filename in ("index.html", "404.html", "emc/index.html", "emc-info/index.html", "robots.txt", "sitemap-index.xml"):
        if not (root / filename).is_file():
            errors.append(f"Missing required output: {filename}")
    if not preview and (root / "robots.txt").is_file():
        if f"Sitemap: {root_url}sitemap-index.xml" not in (root / "robots.txt").read_text():
            errors.append("robots.txt: production sitemap URL missing")

    sitemap_pages = set()
    if (index := root / "sitemap-index.xml").is_file():
        for item in ElementTree.parse(index).findall(".//{*}loc"):
            location = item.text or ""
            check_reference(location, root_url)
            filename = urlsplit(location).path.removeprefix(base)
            if (sitemap := root / filename).is_file():
                sitemap_pages.update(
                    node.text for node in ElementTree.parse(sitemap).findall(".//{*}loc")
                )
    if sitemap_pages != canonical_pages:
        errors.append(
            f"Sitemap URL mismatch. Missing: {sorted(canonical_pages - sitemap_pages)}. "
            f"Unexpected: {sorted(sitemap_pages - canonical_pages)}."
        )

    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Checked {len(pages)} HTML pages for {root_url}")
    if args.list_external:
        print("\n".join(sorted(external)))
    return 0


if __name__ == "__main__":
    sys.exit(main())
