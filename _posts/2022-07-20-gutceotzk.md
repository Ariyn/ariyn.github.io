---
layout: post
title: "고랭의 함수 콜을 정리하는 방법"
date: "2022-07-20T17:37:03+07:00"
lastmod: "2022-07-20T17:37:14+07:00"
slug: "gutceotzk"
permalink: "/posts/gutceotzk/"
kind: dev
section: til
category: library-usage
tags:
  - "TIL"
  - "golang"
---
* Go package의 함수 호출 관계를 보고 싶다면 `callgraph`와 `digraph`를 조합할 수 있다.
  * 먼저 package의 call graph를 digraph 형식으로 만든다.
  * 그 다음 관심 있는 package node만 추리고, 각 node가 호출하는 대상을 뽑는다.

```shell
callgraph -format digraph {package} > /tmp/package.di
digraph nodes /tmp/package.di | grep {package} > /tmp/package_only.di

while read node; do
  echo "{\"name\": \"$node\", \"calls\": $(digraph forward "$node" /tmp/package.di | jq -R | jq -s) }" >> /tmp/nodes.json
done < /tmp/package_only.di
```

* 이렇게 만들면 함수별 호출 목록을 JSON에 가까운 형태로 정리할 수 있다.
  * 시각화하거나, 특정 package 내부 호출만 따로 분석할 때 쓸 수 있다.
* 단, call graph는 분석 방식에 따라 결과가 달라질 수 있다.
  * interface dispatch, reflection, build tag가 얽히면 실제 런타임 호출과 완전히 같지 않을 수 있다.
