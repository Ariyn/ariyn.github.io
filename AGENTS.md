# Repository Instructions

## Blog Writing Workflow

- When the user asks `블로그 글 작성`, `블로그 초안`, `기술 블로그 글로 다듬어`, or asks to write a post in the existing blog tone, use the repo-local skill at `.codex/skills/blog-post-writing`.
- Keep all created or edited workflow files inside this repository. Do not create or modify global Codex, global agent, or other repository files for this workflow.
- For blog writing tasks, read `.codex/skills/blog-post-writing/references/blog-style.md` before drafting the post.
- Reference recent and related files in `_posts/` to confirm the current front matter shape, tone, and formatting, but prefer the style reference file when there is a conflict.
- Edit only the new or explicitly requested post file. Do not modify existing posts in bulk.
- Validate post changes with `bundle exec jekyll build`.
- Do not stage or commit automatically. Only stage and commit when the user explicitly asks, and stage only the files that belong to that task.
- Do not commit `_site` build output.

## Communication

- Use Korean by default unless the user explicitly asks for another language.
- Keep final reports concise and include the post path and validation result when a post is written or edited.
