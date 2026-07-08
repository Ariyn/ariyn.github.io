---
layout: post
title: "zsh에서의 alias -g 옵션"
date: "2024-01-07T19:36:43+07:00"
lastmod: "2024-01-07T22:32:55+07:00"
slug: "udzptctqb"
permalink: "/posts/udzptctqb/"
kind: dev
section: til
category: command
tags:
  - "TIL"
---
zsh의 `alias -g`는 global alias를 만든다.
일반 alias는 명령어의 첫 토큰에서만 확장된다.

{: .tractatus}
1. zsh의 `alias -g`는 global alias를 만든다.

   1. 일반 alias는 명령어의 첫 토큰에서만 확장된다.

   2. global alias는 명령어 중간에서도 확장되기 때문에 파이프나 조건 연산자를 짧게 줄일 수 있다.

      ```shell
          $ cat ~/.zshrc
          alias -g G="| grep"

          $ ls G Do
          Documents Downloads
      ```

2. 이를 응용해서 성공과 실패 알림용 alias를 만들었다.

   ```shell
       $ cat ~/.zshrc

       alias -g ^ns="&& echo " # notify when succeed
       alias -g ^nf="|| echo " # notify when failed

       $ true ^ns "성공하였습니다." ^nf "실패하였습니다."
       성공하였습니다.

       $ false ^ns "성공하였습니다." ^nf "실패하였습니다."
       실패하였습니다.
   ```

   1. 이 덕분에 어떤 명령어 뒤에도 옵션을 붙이는 느낌으로 알림을 추가할 수 있다.

3. 단, `nf`와 `ns`의 순서를 거꾸로 쓰면 의도와 다른 결과가 나온다.

   ```shell
       $ false ^nf failure ^ns succeed
       failure
       succeed
   ```

   1. 앞선 명령어가 실패했기 때문에 `nf = || echo`가 실행된다.

   2. 그런데 `echo failure` 자체는 성공하므로, 뒤따르는 `ns = && echo`도 이어서 실행된다.

   3. 즉 이 방식은 "원래 명령어의 성공/실패"가 아니라 "바로 앞 명령어의 종료 코드"에 계속 반응한다.

4. 그래서 global alias는 짧고 편하지만, 조건 체인을 만들 때는 확장된 실제 명령어를 머릿속으로 한 번 풀어봐야 한다.

   1. 출처: [Zsh tips](https://opensource.com/article/18/9/tips-productivity-zsh)
