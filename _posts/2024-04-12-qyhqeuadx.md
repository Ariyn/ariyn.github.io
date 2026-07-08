---
layout: post
title: "SQS FIFO 큐에서 visibility timeout을 지정해두면, 앞의 메시지가 안 보이는 동안 뒤의 메시지들은 polling되지 않는다."
date: "2024-04-12T16:43:05+07:00"
lastmod: "2024-04-28T20:46:36+07:00"
slug: "qyhqeuadx"
permalink: "/posts/qyhqeuadx/"
kind: dev
section: tech-blog
category: troubleshooting-retrospective
tags:
  - "TIL"
---
SQS FIFO 큐에서는 같은 `MessageGroupId` 안의 메시지 순서가 보장된다.
이 말은 앞 메시지가 처리 중이면, 같은 그룹의 뒤 메시지는 먼저 polling되지 않는다는 뜻이기도 하다.

{: .tractatus}
1. SQS FIFO 큐에서는 같은 `MessageGroupId` 안의 메시지 순서가 보장된다.

   1. 이 말은 앞 메시지가 처리 중이면, 같은 그룹의 뒤 메시지는 먼저 polling되지 않는다는 뜻이기도 하다.

   2. 공식 문서도 "동일한 메시지 그룹 ID에 대한 메시지는 그 메시지를 삭제하거나 다시 표시되는 경우가 아니라면 더 이상 반환되지 않는다"고 설명한다.

   3. 참고: [SQS visibility timeout](https://docs.aws.amazon.com/ko_kr/AWSSimpleQueueService/latest/SQSDeveloperGuide/sqs-visibility-timeout.html#:~:text=%EB%A9%94%EC%8B%9C%EC%A7%80%20%EA%B7%B8%EB%A3%B9%20ID%EA%B0%80%20%EC%9E%88%EB%8A%94%20%EB%A9%94%EC%8B%9C%EC%A7%80%EB%A5%BC%20%EC%88%98%EC%8B%A0%ED%95%9C%20%EA%B2%BD%EC%9A%B0%2C%20%EB%8F%99%EC%9D%BC%ED%95%9C%20%EB%A9%94%EC%8B%9C%EC%A7%80%20%EA%B7%B8%EB%A3%B9%20ID%EC%97%90%20%EB%8C%80%ED%95%9C%20%EB%A9%94%EC%8B%9C%EC%A7%80%EB%8A%94%20%EA%B7%B8%20%EB%A9%94%EC%8B%9C%EC%A7%80%EB%A5%BC%20%EC%82%AD%EC%A0%9C%ED%95%98%EA%B1%B0%EB%82%98%20%EB%A9%94%EC%8B%9C%EC%A7%80%EA%B0%80%20%ED%91%9C%EC%8B%9C%EB%90%98%EB%8A%94%20%EA%B2%BD%EC%9A%B0%EA%B0%80%20%EC%95%84%EB%8B%88%EB%9D%BC%EB%A9%B4%20%EB%8D%94%20%EC%9D%B4%EC%83%81%20%EB%B0%98%ED%99%98%EB%90%98%EC%A7%80%20%EC%95%8A%EC%8A%B5%EB%8B%88%EB%8B%A4.)

2. 그래서 `VisibilityTimeout`을 길게 잡아둔 상태에서 consumer가 메시지를 삭제하지 못하면, 같은 그룹의 뒤 메시지가 멈춘 것처럼 보인다.

   1. 큐 전체가 막힌 것이 아니라 해당 `MessageGroupId`만 막힌 상태일 수 있다.

   2. 다른 `MessageGroupId`를 가진 메시지는 계속 polling될 수 있다.

   3. 순서를 보장하기 위해 같은 그룹 안에서는 앞 메시지 처리가 끝나기 전까지 다음 메시지를 내주지 않는 구조다.

3. 확인할 때는 세 가지를 보면 된다.

   1. 처리 중인 메시지가 삭제되지 않고 visibility timeout 안에 숨어 있는지 확인한다.

   2. 모든 메시지가 같은 `MessageGroupId`를 쓰고 있는지 확인한다.

   3. 순서 보장이 필요 없는 작업까지 같은 그룹으로 묶어 병렬성을 스스로 막고 있지 않은지 확인한다.

4. 결론은 FIFO 큐에서 메시지가 안 나올 때 consumer 수만 늘려서는 해결되지 않을 수 있다는 것이다.

   1. 같은 그룹의 선행 메시지를 삭제하거나 timeout이 끝나야 뒤 메시지가 다시 보인다.

   2. 병렬 처리가 필요하면 의미 있는 단위로 `MessageGroupId`를 나눠야 한다.
