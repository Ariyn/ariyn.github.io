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
* Gorm에서 MySQL의 `created_at` 같은 시간 컬럼을 `time.Time`으로 읽다가 scan 오류가 나면 connection string을 확인한다.
  * 대표적인 해결은 DSN 뒤에 `parseTime=true`를 붙이는 것이다.
  * 예시는 `user:pass@tcp(localhost:3306)/db?parseTime=true`다.
* 이 옵션이 없으면 MySQL driver가 시간 값을 `[]uint8` 같은 형태로 넘기고, Go의 `time.Time`으로 바로 scan 하지 못할 수 있다.
  * 그래서 오류 메시지에 `unsupported Scan`과 `type []uint8 into type *time.Time`이 같이 나온다.
* 이미 다른 query parameter가 있다면 `?`가 아니라 `&parseTime=true`로 이어 붙여야 한다.
  * DSN을 만들 때 문자열을 직접 이어 붙이면 이 부분을 실수하기 쉽다.
