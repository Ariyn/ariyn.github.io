---
layout: post
title: "godot에서 signal을 변수와 함께 쓰기"
date: "2021-11-24T21:51:52+07:00"
lastmod: "2021-11-24T21:52:11+07:00"
slug: "napcywbps"
permalink: "/posts/napcywbps/"
kind: dev
section: til
category: configuration-note
tags:
  - "TIL"
  - "godot"
---
* Godot signal은 인자를 함께 보낼 수 있다.
  * signal 선언부에 인자 이름을 적어두면, emit할 때 값을 같이 넘길 수 있다.

```gdscript
signal my_signal(value, value2)
```

* 이렇게 해두면 signal을 받는 쪽에서 어떤 값이 전달되는지 구조를 알기 쉽다.
  * 예를 들어 충돌한 객체, 점수, 상태값 같은 정보를 signal과 함께 넘길 수 있다.
* signal은 호출 방향을 느슨하게 만들 때 유용하다.
  * 노드끼리 직접 서로를 강하게 참조하지 않아도, 이벤트와 필요한 값만 전달할 수 있다.
