---
layout: post
title: "unaddressable value문제"
date: "2021-11-13T17:21:13+07:00"
lastmod: "2021-11-13T17:22:43+07:00"
slug: "ubfwpramn"
permalink: "/posts/ubfwpramn/"
kind: dev
tags:
  - "TIL"
  - "golang"
  - "gorm"
---
* reflect: reflect.Value.Set using unaddressable value
  * `db.Create(v)`에서 v가 값으로 복사되는지 확인하자. pointer가 들어가야 한다.
    * 올바른 예: `db.Create(&v)`
    * 잘못된 예: `db.Create(v)`
