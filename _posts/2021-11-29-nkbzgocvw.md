---
layout: post
title: "스케쥴러 실행시, 테이블이 없어서 실행되지 않는 경우"
date: "2021-11-29T09:59:56+07:00"
lastmod: "2021-12-03T23:42:54+07:00"
slug: "nkbzgocvw"
permalink: "/posts/nkbzgocvw/"
tags:
  - "airflow"
  - "TIL"
---
* `WARNING - Failed to log action with (sqlite3.OperationalError) no such table: log`
  * airflow_home이 잘 설정되어 있는지 보고, `airflow db init`를 하자
    * 기본적으로는 `~/airflow`로 설정되는듯
