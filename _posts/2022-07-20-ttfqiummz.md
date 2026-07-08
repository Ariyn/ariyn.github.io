---
layout: post
title: "`jq -R . | jq -s`"
date: "2022-07-20T15:40:34+07:00"
lastmod: "2022-07-20T16:52:31+07:00"
slug: "ttfqiummz"
permalink: "/posts/ttfqiummz/"
kind: dev
section: til
category: command
tags:
  - "TIL"
  - "bash"
---
* 여러 줄짜리 텍스트를 JSON array로 바꾸고 싶을 때 `jq -R . | jq -s`를 사용할 수 있다.
  * `-R`은 입력을 JSON으로 파싱하지 않고 raw string으로 읽는다.
  * 첫 번째 `jq -R .`는 각 줄을 JSON string으로 만든다.
  * 두 번째 `jq -s`는 여러 JSON 값을 하나의 배열로 묶는다.
* 예를 들어 줄 단위 명령 결과를 API 요청 body로 넘겨야 할 때 유용하다.
  * shell 출력은 기본적으로 그냥 텍스트라서, JSON array가 필요한 곳에 바로 넣기 어렵다.
* 같은 과정을 한 번에 쓰면 `jq -R -s 'split("\n")'` 같은 방식도 가능하다.
  * 다만 마지막 개행 처리까지 신경 써야 하므로, 줄 단위로 먼저 만들고 `-s`로 묶는 방식이 읽기 쉽다.
