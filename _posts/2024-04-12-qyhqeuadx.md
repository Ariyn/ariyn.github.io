---
layout: post
title: "SQS fifo 큐에서 aviliability 타임을 지정해두면, 앞의 메시지가 안보이는 동안 뒤의 메시지들은 polling되지 않는다."
date: "2024-04-12T16:43:05+07:00"
lastmod: "2024-04-28T20:46:36+07:00"
slug: "qyhqeuadx"
permalink: "/posts/qyhqeuadx/"
kind: dev
tags:
  - "TIL"
---
* 공식 문서의 내용 - [메시지 그룹 ID가 있는 메시지를 수신한 경우, 동일한 메시지 그룹 ID에 대한 메시지는 그 메시지를 삭제하거나 메시지가 표시되는 경우가 아니라면 더 이상 반환되지 않습니다.](https://docs.aws.amazon.com/ko_kr/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html#:~:text=%EB%A9%94%EC%8B%9C%EC%A7%80%20%EA%B7%B8%EB%A3%B9%20ID%EA%B0%80%20%EC%9E%88%EB%8A%94%20%EB%A9%94%EC%8B%9C%EC%A7%80%EB%A5%BC%20%EC%88%98%EC%8B%A0%ED%95%9C%20%EA%B2%BD%EC%9A%B0%2C%20%EB%8F%99%EC%9D%BC%ED%95%9C%20%EB%A9%94%EC%8B%9C%EC%A7%80%20%EA%B7%B8%EB%A3%B9%20ID%EC%97%90%20%EB%8C%80%ED%95%9C%20%EB%A9%94%EC%8B%9C%EC%A7%80%EB%8A%94%20%EA%B7%B8%20%EB%A9%94%EC%8B%9C%EC%A7%80%EB%A5%BC%20%EC%82%AD%EC%A0%9C%ED%95%98%EA%B1%B0%EB%82%98%20%EB%A9%94%EC%8B%9C%EC%A7%80%EA%B0%80%20%ED%91%9C%EC%8B%9C%EB%90%98%EB%8A%94%20%EA%B2%BD%EC%9A%B0%EA%B0%80%20%EC%95%84%EB%8B%88%EB%9D%BC%EB%A9%B4%20%EB%8D%94%20%EC%9D%B4%EC%83%81%20%EB%B0%98%ED%99%98%EB%90%98%EC%A7%80%20%EC%95%8A%EC%8A%B5%EB%8B%88%EB%8B%A4.)
    * 메시지 그룹 ID를 바꿔준다면 해당 그룹의 메시지들은 계속 나온다.
  * 따라서 fifo 큐를 쓰고 있는데 메시지가 안나온다면 당황하지 말고 확인해보자.
