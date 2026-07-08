---
layout: post
title: "logstash에서 사용하는 json, grok등등의 이름"
date: "2021-11-03T14:31:05+07:00"
lastmod: "2021-11-03T14:31:40+07:00"
slug: "ygybygxfk"
permalink: "/posts/ygybygxfk/"
kind: dev
section: til
category: configuration-note
tags:
  - "TIL"
  - "logstash"
---
* Logstash에서 `file`, `grok`, `json` 같은 것은 plugin으로 부른다.
  * 입력 단계에 쓰이면 input plugin이다.
  * 가공 단계에 쓰이면 filter plugin이다.
  * 출력 단계에 쓰이면 output plugin이다.
* 예를 들어 `file`은 file input plugin이고, `grok`은 grok filter plugin이다.
  * 문서를 찾을 때도 이 이름으로 검색하면 공식 문서를 찾기 쉽다.
* Logstash pipeline을 읽을 때는 plugin 종류를 먼저 나누면 구조가 보인다.
  * input은 어디서 가져오는가.
  * filter는 어떻게 파싱하고 변환하는가.
  * output은 어디로 보내는가.
