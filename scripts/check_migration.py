#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path

ALLOWED_KINDS = {"dev", "personal"}


def main() -> None:
    site_root = Path(sys.argv[1]) if len(sys.argv) > 1 else Path("_site")
    posts_json = json.loads((site_root / "posts.json").read_text())
    post_dirs = {
        path.name
        for path in (site_root / "posts").iterdir()
        if path.is_dir() and (path / "index.html").exists()
    }
    missing = sorted(set(posts_json) - post_dirs)
    extra = sorted(post_dirs - set(posts_json))
    print(f"posts.json count: {len(posts_json)}")
    print(f"post page count: {len(post_dirs)}")
    if missing:
        print("missing post pages:")
        for slug in missing:
            print(f"  {slug}")
    if extra:
        print("extra post pages:")
        for slug in extra:
            print(f"  {slug}")
    kind_errors = find_kind_errors(Path("_posts"))
    if kind_errors:
        print("kind metadata errors:")
        for error in kind_errors:
            print(f"  {error}")
    if len(posts_json) != len(post_dirs) or missing or extra or kind_errors:
        raise SystemExit(1)


def find_kind_errors(posts_root: Path) -> list[str]:
    errors: list[str] = []
    for post_path in sorted(posts_root.glob("*.md")):
        front_matter = read_front_matter(post_path)
        kinds = [
            line.split(":", 1)[1].strip()
            for line in front_matter.splitlines()
            if line.startswith("kind:")
        ]
        if len(kinds) != 1:
            errors.append(f"{post_path}: expected exactly one kind, found {len(kinds)}")
        elif kinds[0] not in ALLOWED_KINDS:
            errors.append(f"{post_path}: invalid kind {kinds[0]!r}")
    return errors


def read_front_matter(path: Path) -> str:
    text = path.read_text()
    if not text.startswith("---\n"):
        return ""
    return text.split("---", 2)[1]


if __name__ == "__main__":
    main()
