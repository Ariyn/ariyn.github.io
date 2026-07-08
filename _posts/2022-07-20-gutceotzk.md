---
layout: post
title: "고랭의 함수 콜을 정리하는 방법"
date: "2022-07-20T17:37:03+07:00"
lastmod: "2022-07-20T17:37:14+07:00"
slug: "gutceotzk"
permalink: "/posts/gutceotzk/"
tags:
  - "TIL"
  - "golang"
---
```shell
  > callgraph -format digraph {package} > /tmp/package.di
  
  > cat /tmp/package.di | digraph nodes | grep {package} > /tmp/package_only.di
  
  > while read node; do
  echo "{\"name\": \"$node\", \"calls\": $(cat /tmp/package.di | digraph forward "$node" | jq -R | jq -s) }" >> /tmp/nodes.json;
  done < /tmp/package_only.di
  ```
