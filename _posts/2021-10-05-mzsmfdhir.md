---
layout: post
title: "beanstalk에서 /etc/hosts를 수정하는 방법"
date: "2021-10-05T18:29:53+07:00"
lastmod: "2021-10-05T18:31:16+07:00"
slug: "mzsmfdhir"
permalink: "/posts/mzsmfdhir/"
kind: dev
section: til
category: configuration-note
tags:
  - "TIL"
  - "aws"
  - "beanstalk"
---
.ebextensions에 커맨드를 추가.
핵심은 필요한 판단과 확인 지점을 짧은 명제로 남기는 것이다.

{: .tractatus}
1. https://docs.aws.amazon.com/ko_kr/elasticbeanstalk/latest/dg/ebextensions.html

   1. .ebextensions에 커맨드를 추가

      ```yaml
          command:
            echo '127.0.0.1 hostname' >> /etc/hosts
      ```

   2. https://stackoverflow.com/questions/41903297/how-to-customize-hosts-file-in-elastic-beanstalk

   3. https://namocom.tistory.com/825
