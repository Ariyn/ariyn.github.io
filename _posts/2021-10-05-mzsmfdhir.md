---
layout: post
title: "beanstalk에서 /etc/hosts를 수정하는 방법"
date: "2021-10-05T18:29:53+07:00"
lastmod: "2021-10-05T18:31:16+07:00"
slug: "mzsmfdhir"
permalink: "/posts/mzsmfdhir/"
tags:
  - "TIL"
  - "aws"
  - "beanstalk"
---
* https://docs.aws.amazon.com/ko_kr/elasticbeanstalk/latest/dg/ebextensions.html
  * .ebextensions에 커맨드를 추가
    ```javascript
    command:
      echo '127.0.0.1 hostname' >> /etc/hosts
    ```

    * https://stackoverflow.com/questions/41903297/how-to-customize-hosts-file-in-elastic-beanstalk
    * https://namocom.tistory.com/825
