---
layout: post
title: "unaddressable value문제"
date: "2021-11-13T17:21:13+07:00"
lastmod: "2021-11-13T17:22:43+07:00"
slug: "ubfwpramn"
permalink: "/posts/ubfwpramn/"
kind: dev
section: til
category: short-error-fix
tags:
  - "TIL"
  - "golang"
  - "gorm"
---
* Gorm에서 `reflect: reflect.Value.Set using unaddressable value`가 나오면 값이 addressable한지 확인해야 한다.
  * `db.Create(v)`처럼 값을 그대로 넘기면 Gorm이 필드를 설정해야 하는 시점에 주소를 잡지 못할 수 있다.
  * 생성이나 업데이트 과정에서 struct field를 수정해야 하므로 pointer가 필요하다.
* 기본 대응은 pointer를 넘기는 것이다.
  * 올바른 예: `db.Create(&v)`
  * 잘못된 예: `db.Create(v)`
* 이 오류는 reflection을 쓰는 라이브러리에서 자주 보인다.
  * 라이브러리가 값을 읽기만 하는지, 내부 필드를 수정해야 하는지에 따라 pointer 필요 여부가 달라진다.
  * Gorm model을 넘길 때는 우선 pointer를 기본으로 생각하는 편이 안전하다.
