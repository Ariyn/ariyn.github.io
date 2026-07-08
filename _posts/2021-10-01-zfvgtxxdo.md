---
layout: post
title: "beanstalk에서 golang을 사용할 때 주의할 점"
date: "2021-10-01T12:07:36+07:00"
lastmod: "2021-12-01T23:24:54+07:00"
slug: "zfvgtxxdo"
permalink: "/posts/zfvgtxxdo/"
tags:
  - "TIL"
  - "golang"
  - "beanstalk"
---
* golang을 사용할 때, 몇가지 옵션을 사용할 수 있다.
    * Buildfile을 사용한 빌드
    * application.go를 자동으로 빌드
    * bin/application 바이너리를 사용
      * root에 Procfile이 필수
  * 이때 주의할 점은, 앞에서 하나라도 만족되면 이후 것들이 진행되지 않는다.
    * 따라서 application.go가 있다면, Procfile에서 bin/application을 실행하라고 해도 실행되지 않는다.
  * 로그에서 확인 할 것
    * no Buildfile found, checking application.go file
    * 이런식으로 계속 있을것.
    * 어디까지 로그가 찍혀 있는지 확인필요
