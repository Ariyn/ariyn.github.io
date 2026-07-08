---
name: blog-post-writing
description: Write, revise, and verify posts for this Jekyll blog. Use when the user asks in Korean or English to write a blog post, draft a blog article, turn notes into a technical blog post, match the existing blog tone, or says phrases such as "블로그 글 작성", "블로그 초안", "기술 블로그 글로 다듬어", or "기존 글 톤으로 포스트 작성".
---

# Blog Post Writing

## Required References

- Read `references/blog-style.md` before drafting or revising a post.
- Inspect `_config.yml` and a few recent or related files in `_posts/` to confirm current front matter and formatting.
- Use the reference file as the primary style contract when examples differ.

## Workflow

1. Identify the post topic, intended angle, and any source notes from the user request.
2. Choose a short English kebab-case slug if the user did not provide one.
3. Create or edit exactly one post file unless the user explicitly asks for more.
   - New post path: `_posts/<YYYY-MM-DD>-<slug>.md`.
   - Use the current date from the environment for `date` and `lastmod`.
4. Write Jekyll front matter using the repository format.
5. Draft the body in the existing blog style:
   - Korean technical blog tone.
   - `*` bullet-first structure.
   - 2-space indented nested bullets.
   - Short judgment, reason, implementation detail, validation, and lesson learned.
6. Run `bundle exec jekyll build` after writing or revising.
7. Report the changed file path and build result.

## Guardrails

- Keep all workflow files and generated posts inside this repository.
- Do not create or modify global `~/.codex`, `~/.agents`, or other repository files.
- Do not automatically stage or commit. Only stage or commit when the user explicitly asks.
- Do not modify existing posts in bulk.
- Do not commit `_site` build output.
- Do not refactor layouts, scripts, or site configuration unless the user explicitly asks.
- If the working tree already has unrelated changes, leave them untouched and mention only relevant risk.

## Validation

- Run `bundle exec jekyll build`.
- Check `git status --short` after the build.
- Confirm the intended post file is the only newly edited file from this task, ignoring pre-existing unrelated changes.
- If the build writes `_site`, do not stage it.
