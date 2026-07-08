---
layout: post
title: "스케쥴러 실행시, 테이블이 없어서 실행되지 않는 경우"
date: "2021-11-29T09:59:56+07:00"
lastmod: "2021-12-03T23:42:54+07:00"
slug: "nkbzgocvw"
permalink: "/posts/nkbzgocvw/"
kind: dev
tags:
  - "airflow"
  - "TIL"
---
* Airflow scheduler 실행 중 `no such table: log`가 나오면 metadata DB 초기화를 의심해야 한다.
  * 예시 경고는 `WARNING - Failed to log action with (sqlite3.OperationalError) no such table: log`다.
  * Airflow가 로그를 기록하려는데 metadata DB에 필요한 테이블이 없는 상태다.
* 먼저 `AIRFLOW_HOME`이 의도한 위치인지 확인한다.
  * 기본값은 보통 `~/airflow`라서, 실행 환경이 바뀌면 다른 DB 파일을 보고 있을 수 있다.
* 그 다음 metadata DB 초기화를 실행한다.
  * 오래된 Airflow에서는 `airflow db init`을 사용했다.
  * 버전에 따라 초기화 또는 migration 명령이 달라질 수 있으므로 현재 Airflow 버전의 명령을 확인해야 한다.
* 핵심은 scheduler 문제가 아니라 DB schema 준비 문제일 수 있다는 점이다.
