#!/usr/bin/env python3
from __future__ import annotations

import json
import sys
from pathlib import Path


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
    if len(posts_json) != 286 or missing:
        raise SystemExit(1)


if __name__ == "__main__":
    main()
