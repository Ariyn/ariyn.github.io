---
layout: post
title: "golang에서 regexp를 사용할 때, 여러 라인에 걸쳐 읽으려면 `(?s)`를 붙여 줘야 한다."
date: "2021-09-10T22:36:56+07:00"
lastmod: "2021-09-17T10:04:02+07:00"
slug: "hcgnzjtrl"
permalink: "/posts/hcgnzjtrl/"
kind: dev
tags:
  - "TIL"
  - "regexp"
  - "golang"
---
```javascript
  regexp.MustCompile(`(?s)START(.*?)STOP`)
  ```

  * 만약 `(?m)`과 함께 쓰려면?
    ```javascript
    `(?sm)START(.*?)STOP` 
    ```
