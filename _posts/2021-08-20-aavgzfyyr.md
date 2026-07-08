---
layout: post
title: "--preferred-challenges dns"
date: "2021-08-20T14:56:45+07:00"
lastmod: "2021-12-01T22:36:24+07:00"
slug: "aavgzfyyr"
permalink: "/posts/aavgzfyyr/"
kind: dev
section: til
category: link-short-summary
tags:
  - "lets encrypt"
  - "TIL"
---
* `--preferred-challenges dns`는 Certbot에서 DNS challenge를 우선 사용하겠다는 옵션이다.
  * Let’s Encrypt 인증 과정에서 HTTP 파일 검증 대신 DNS TXT 레코드 검증을 쓰고 싶을 때 사용한다.
  * 서버의 80번 포트를 열기 어렵거나 wildcard 인증서를 다룰 때 DNS 방식이 필요할 수 있다.
* 실제 사용 가능 여부는 설치된 플러그인과 실행 방식에 따라 달라진다.
  * DNS provider 플러그인이 있으면 TXT 레코드 생성을 자동화할 수 있다.
  * 플러그인이 없으면 수동으로 TXT 레코드를 추가해야 할 수 있다.
* challenge 방식은 대략 `http`와 `dns` 중 어느 쪽으로 도메인 소유를 증명할지의 문제다.
  * 운영 환경에서는 인증서 갱신 자동화까지 같이 생각해야 한다.
