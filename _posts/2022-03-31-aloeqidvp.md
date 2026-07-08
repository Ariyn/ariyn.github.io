---
layout: post
title: "generic은 여러개 쓸 수 있다"
date: "2022-03-31T23:30:37+07:00"
lastmod: "2022-03-31T23:35:41+07:00"
slug: "aloeqidvp"
permalink: "/posts/aloeqidvp/"
kind: dev
section: til
category: library-usage
tags:
  - "TIL"
  - "rust"
---
* Rust generic type parameter는 하나만 쓸 필요가 없다.
  * 필요한 만큼 여러 개를 선언할 수 있다.

```rust
struct Foo<T, U> {
    x: T,
    y: U,
}
```

* 위 예시에서 `x`와 `y`는 서로 다른 타입을 가질 수 있다.
  * 예를 들어 `Foo<i32, String>`처럼 사용할 수 있다.
* 다만 generic parameter가 너무 많아지면 타입 설계가 복잡해졌다는 신호일 수 있다.
  * 여러 타입을 정말 독립적으로 받아야 하는지, trait이나 별도 struct로 나누는 편이 나은지 같이 봐야 한다.
