---
layout: post
title: "golang에서 regexp를 사용할 때, 여러 라인에 걸쳐 읽으려면 `(?s)`를 붙여 줘야 한다."
date: "2021-09-10T22:36:56+07:00"
lastmod: "2021-09-17T10:04:02+07:00"
slug: "hcgnzjtrl"
permalink: "/posts/hcgnzjtrl/"
kind: dev
section: til
category: command
tags:
  - "TIL"
  - "regexp"
  - "golang"
---
* Go의 `regexp`에서 `.`은 기본적으로 newline을 매칭하지 않는다.
  * 여러 줄에 걸친 문자열을 `.*?` 같은 패턴으로 잡고 싶다면 `(?s)` 플래그를 붙인다.
  * `(?s)`는 dot이 newline까지 포함해 매칭되도록 만든다.

```go
regexp.MustCompile(`(?s)START(.*?)STOP`)
```

* multi-line anchor 동작까지 같이 바꾸고 싶다면 `(?m)`과 함께 쓸 수 있다.

```go
regexp.MustCompile(`(?sm)START(.*?)STOP`)
```

* `(?s)`와 `(?m)`은 역할이 다르다.
  * `(?s)`는 `.`이 newline을 포함할지에 영향을 준다.
  * `(?m)`은 `^`, `$`가 줄 단위 경계로 동작할지에 영향을 준다.
