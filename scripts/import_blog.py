#!/usr/bin/env python3
from __future__ import annotations

import argparse
import json
import re
import shutil
from pathlib import Path


IMAGE_SUFFIXES = {".png", ".jpg", ".jpeg", ".gif", ".webp"}


def main() -> None:
    parser = argparse.ArgumentParser(description="Import raw blog markdown into Jekyll posts.")
    parser.add_argument("--blog-root", required=True)
    parser.add_argument("--site-root", default=".")
    args = parser.parse_args()

    site_root = Path(args.site_root).resolve()
    blog_root = Path(args.blog_root).resolve()
    posts_root = site_root / "_posts"

    if not blog_root.exists():
        raise SystemExit(f"blog root does not exist: {blog_root}")

    source_posts = list(blog_root.glob("*.md"))

    reset_directory(posts_root)
    for source_post in sorted(source_posts, key=lambda path: path.name.lower()):
        write_imported_post(posts_root, source_post)

    copy_image_assets(blog_root, site_root)

    print(f"imported markdown posts: {len(source_posts)}")
    print(f"total _posts files: {len(list(posts_root.glob('*.md')))}")


def reset_directory(path: Path) -> None:
    if path.exists():
        shutil.rmtree(path)
    path.mkdir(parents=True, exist_ok=True)


def write_imported_post(posts_root: Path, source_post: Path) -> None:
    front_matter, body = split_front_matter(source_post.read_text())
    slug = source_post.stem.lower()
    post = {
        "slug": slug,
        "title": front_matter["title"],
        "date": front_matter["date"],
        "lastmod": front_matter.get("lastmod", front_matter["date"]),
        "tags": front_matter.get("tags", []),
        "body": body.strip() + "\n",
    }
    write_post(posts_root, post)


def write_post(posts_root: Path, post: dict[str, object]) -> None:
    date = str(post["date"])
    slug = str(post["slug"])
    filename = f"{date[:10]}-{slug}.md"
    front_matter = [
        "---",
        "layout: post",
        f"title: {yaml_string(str(post['title']))}",
        f"date: {yaml_string(date)}",
        f"lastmod: {yaml_string(str(post['lastmod']))}",
        f"slug: {yaml_string(slug)}",
        f"permalink: {yaml_string(f'/posts/{slug}/')}",
        "tags:",
    ]
    for tag in post.get("tags", []):
        front_matter.append(f"  - {yaml_string(str(tag))}")
    front_matter.append("---")
    content = "\n".join(front_matter) + "\n" + str(post["body"]).strip() + "\n"
    (posts_root / filename).write_text(content)


def split_front_matter(text: str) -> tuple[dict[str, object], str]:
    if not text.startswith("---\n"):
        raise ValueError("missing front matter")

    _, front, body = text.split("---", 2)
    data: dict[str, object] = {}
    current_list: str | None = None

    for line in front.splitlines():
        if not line.strip():
            continue
        if line.startswith("  - ") and current_list:
            data.setdefault(current_list, []).append(unquote_yaml(line[4:].strip()))
            continue
        current_list = None
        key, _, value = line.partition(":")
        if not _:
            continue
        key = key.strip()
        value = value.strip()
        if value:
            data[key] = unquote_yaml(value)
        else:
            data[key] = []
            current_list = key

    return data, body


def copy_image_assets(blog_root: Path, site_root: Path) -> None:
    asset_dirs = {
        path.parent
        for path in blog_root.rglob("*")
        if path.is_file() and path.suffix.lower() in IMAGE_SUFFIXES
    }
    for asset_dir in sorted(asset_dirs, key=lambda path: path.name.lower()):
        target = site_root / asset_dir.name
        if target.exists():
            shutil.rmtree(target)
        shutil.copytree(asset_dir, target)


def yaml_string(value: str) -> str:
    return json.dumps(value, ensure_ascii=False)


def unquote_yaml(value: str) -> str:
    if len(value) >= 2 and value[0] == value[-1] and value[0] in {"'", '"'}:
        return value[1:-1]
    return value


if __name__ == "__main__":
    main()
