---
layout: post
title: "generic은 여러개 쓸 수 있다"
date: "2022-03-31T23:30:37+07:00"
lastmod: "2022-03-31T23:35:41+07:00"
slug: "aloeqidvp"
permalink: "/posts/aloeqidvp/"
kind: dev
tags:
  - "TIL"
  - "rust"
---
* 단 너무 많이 쓰면 문제의 신호일 수 있을것
  ```rust
  struct Foo<T,U> {
    x: T,
    y: U,
  }
  ```
