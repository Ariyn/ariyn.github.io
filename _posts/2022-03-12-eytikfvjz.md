---
layout: post
title: "gorm을 쓸 때, `sql: Scan error on column index 1, name \\\"created_at\\\": unsupported Scan, storing driver.Value type []uint8 into type *time.Time` 오류가 나는 경우"
date: "2022-03-12T19:44:27+07:00"
lastmod: "2022-03-12T19:44:51+07:00"
slug: "eytikfvjz"
permalink: "/posts/eytikfvjz/"
kind: dev
tags:
  - "TIL"
  - "gorm"
---
* sql connection string의 제일 뒤에, `?parseTime=true`를 붙여주자
