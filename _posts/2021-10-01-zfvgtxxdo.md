---
layout: post
title: "beanstalk에서 golang을 사용할 때 주의할 점"
date: "2021-10-01T12:07:36+07:00"
lastmod: "2021-12-01T23:24:54+07:00"
slug: "zfvgtxxdo"
permalink: "/posts/zfvgtxxdo/"
kind: dev
tags:
  - "TIL"
  - "golang"
  - "beanstalk"
---
* Elastic Beanstalk에서 Go 애플리케이션을 배포할 때는 실행 방식을 자동으로 판별한다.
  * `Buildfile`을 사용한 빌드
  * `application.go` 자동 빌드
  * `bin/application` 바이너리 실행
  * `Procfile` 기반 실행
* 주의할 점은 앞 단계 조건이 만족되면 뒤 단계가 실행되지 않을 수 있다는 것이다.
  * 예를 들어 `application.go`가 있으면, `Procfile`에서 `bin/application`을 실행하라고 적어도 기대한 경로로 가지 않을 수 있다.
  * 파일 이름 하나가 배포 동작을 바꾸는 셈이다.
* 문제를 확인할 때는 배포 로그를 봐야 한다.
  * `no Buildfile found, checking application.go file` 같은 로그가 어디까지 찍혔는지 확인한다.
  * Beanstalk가 어떤 배포 방식을 선택했는지 로그에서 먼저 확정해야 한다.
* 배포 방식을 명시하고 싶다면 불필요한 후보 파일을 두지 않는 것이 좋다.
  * 자동 감지는 편하지만, 여러 방식의 흔적이 섞이면 오히려 예측하기 어려워진다.
