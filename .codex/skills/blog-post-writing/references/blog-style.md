# Blog Style Reference

## Voice

- Write in Korean by default.
- Use a concise technical blog tone, not a marketing tone.
- Prefer direct observations and practical judgments over broad reflection.
- Explain why a choice was made, what changed, how it was verified, and what should be remembered next time.
- For retrospective posts, focus on selection criteria, implementation details, validation, and lessons learned.

## Body Format

- Use `*` as the top-level bullet marker.
- Use 2 spaces for nested bullet indentation.
- Keep paragraphs short.
- Use inline code for file names, commands, identifiers, and tools.
- Avoid large section headings unless the post clearly needs them.
- Do not over-explain common tools. Explain only what matters for this migration, bug, or technical decision.

Example:

```md
* 먼저 문제는 배포 흐름이 복잡하다는 것이었다.
  * 글을 쓰는 일보다 빌드와 배포를 신경 쓰는 시간이 더 커졌다.
  * 그래서 GitHub Pages와 맞는 구조로 줄이는 것이 목표였다.
* 작업은 크게 세 가지였다.
  * front matter를 Jekyll 형식으로 맞췄다.
  * 기존 permalink를 유지했다.
  * 마지막으로 `bundle exec jekyll build`로 확인했다.
```

## Front Matter

- Use the existing Jekyll post format.
- Include `kind: dev` for technical/development posts unless nearby related posts show a better value.
- Use quoted strings for scalar values, matching existing files.
- Use environment current date for new posts.
- Use `Asia/Bangkok` offset style from existing posts unless the user explicitly asks otherwise.

Template:

```yaml
---
layout: post
title: "POST_TITLE"
date: "YYYY-MM-DDT00:00:00+07:00"
lastmod: "YYYY-MM-DDT00:00:00+07:00"
slug: "post-slug"
permalink: "/posts/post-slug/"
kind: dev
tags:
  - "블로그"
  - "개발"
---
```

## Slug And File Name

- File name: `_posts/YYYY-MM-DD-slug.md`.
- Use a short English kebab-case slug.
- Keep slug stable once a post is created.
- If the user provides a slug, use it unless it conflicts with an existing post.

## Content Shape

- Start with the context or original reason for the work.
- Then describe the decision or change.
- Then describe the concrete implementation details.
- Include validation when the post is about a migration, refactor, tool change, or operational workflow.
- End with a compact takeaway.

Recommended order:

1. Previous state
2. Reason for change
3. What changed
4. What was tricky
5. How it was verified
6. Final takeaway

## Validation Notes

- `bundle exec jekyll build` passing only proves the site renders. It does not prove content fidelity.
- For migration posts, mention content validation separately when relevant:
  - source and target slug list comparison
  - front matter excluded body hash comparison
  - internal link and image path comparison
  - rendered article text/link/image comparison

## Reporting

- Final response should mention:
  - the post file path
  - whether `bundle exec jekyll build` passed
  - any unrelated pre-existing working tree changes that were left untouched
- Do not say a commit was made unless the user explicitly asked for a commit and it actually succeeded.
