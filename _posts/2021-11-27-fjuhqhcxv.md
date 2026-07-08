---
layout: post
title: "godot에서 타일셋의 콜리젼이 안보이거나 선택이 안될때"
date: "2021-11-27T16:45:43+07:00"
lastmod: "2021-12-03T23:41:52+07:00"
slug: "fjuhqhcxv"
permalink: "/posts/fjuhqhcxv/"
kind: dev
tags:
  - "godot"
  - "TIL"
---
* Godot에서 TileSet collision이 안 보이거나 선택되지 않을 때는 먼저 editor 표시 상태를 의심해 볼 수 있다.
  * 당시 메모 기준으로는 스크롤이나 zoom을 크게 바꿨다가 다시 줄이면 보이는 경우가 있었다.
  * 실제 데이터가 사라진 것이 아니라 editor 표시가 꼬인 상태일 수 있다.
* 이런 문제는 곧바로 설정을 갈아엎기 전에 화면 갱신을 먼저 시도하는 편이 낫다.
  * zoom 변경, 다른 타일 선택, editor 재시작처럼 비용이 낮은 확인부터 한다.
* 그래도 안 되면 collision shape가 실제로 저장되어 있는지 확인해야 한다.
  * 표시 문제와 데이터 누락 문제를 구분해야 삽질이 줄어든다.
