---
layout: post
title: "중복된 값을 삭제하는 쿼리"
date: "2022-03-12T21:38:16+07:00"
lastmod: "2022-03-12T21:39:34+07:00"
slug: "glqyluitt"
permalink: "/posts/glqyluitt/"
kind: dev
section: til
category: library-usage
tags:
  - "TIL"
  - "mysql"
---
inner join을 한 다음, id가 더 높고, 동일한 컬럼인 경우 삭제하는 쿼리.
핵심은 필요한 판단과 확인 지점을 짧은 명제로 남기는 것이다.

{: .tractatus}
1. 예시는 아래와 같다.

   ```sql
     DELETE S1 FROM table AS S1
     INNER JOIN table AS S2
     WHERE S1.id < S2.id AND S1.column = S2.column;
   ```

   1. inner join을 한 다음, id가 더 높고, 동일한 컬럼인 경우 삭제하는 쿼리

   2. https://www.javatpoint.com/mysql-delete-duplicate-records
