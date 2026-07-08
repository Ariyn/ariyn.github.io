---
layout: post
title: "~/.zprofile"
date: "2021-12-23T21:49:42+07:00"
lastmod: "2021-12-23T21:49:56+07:00"
slug: "kzstscfvn"
permalink: "/posts/kzstscfvn/"
kind: dev
tags:
  - "TIL"
  - "mac"
  - "shell"
---
* `~/.zprofile`은 zsh의 login shell에서 읽히는 설정 파일이다.
  * macOS Terminal은 새 창을 login shell로 여는 경우가 많아서, 터미널을 처음 열 때 이 파일이 실행될 수 있다.
  * PATH처럼 세션 시작 시 한 번 잡아야 하는 설정을 여기에 둘 수 있다.
* 대화형 shell 설정은 보통 `~/.zshrc`에 둔다.
  * 그래서 `~/.zprofile`에서 `. ~/.zshrc`를 호출해 같은 설정을 읽게 만들기도 한다.
* 다만 무조건 합치는 것이 정답은 아니다.
  * login shell에서만 필요한 설정과 매번 새 shell마다 필요한 설정을 구분하면 중복 실행 문제를 줄일 수 있다.
