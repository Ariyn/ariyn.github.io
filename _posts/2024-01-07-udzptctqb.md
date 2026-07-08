---
layout: post
title: "zsh에서의 alias -g 옵션"
date: "2024-01-07T19:36:43+07:00"
lastmod: "2024-01-07T22:32:55+07:00"
slug: "udzptctqb"
permalink: "/posts/udzptctqb/"
kind: dev
tags:
  - "TIL"
---
* -g 옵션을 준다면, 명령어의 처음이 아니라 어느 부분에서나 사용할 수 있다.
    ```shell
    $ cat ~/.zshrc
    alias -g G="| grep"
    
    $ ls G Do
    Documents Downloads
    ```

  * 이를 응용해서 ns와 nf를 만들었다.
    ```shell
    $ cat ~/.zshrc
    
    alias -g ^ns="&& echo " # notify when succeed
    alias -g ^nf="|| echo " # notify when failed
    
    $ true ^ns "성공하였습니다." ^nf "실패하였습니다."
    성공하였습니다.
    
    $ false ^ns "성공하였습니다." ^nf "실패하였습니다."
    실패하였습니다.
    ```

    * 이 덕분에 어느 명령어든지 옵션을 추가하는 것 처럼 노티를 사용할 수 있다.
  * nf와 ns의 순서를 거꾸로 쓰면 생각치 못한 버그가 있다
    ```shell
    $ false ^nf failure ^ns succeed
    failure
    succeed
    ```

    * 앞선 명령어가 실패했기 때문에 `nf = || echo`가 실행된다.
그리고 echo 가 정상적으로 실행되었기 때문에 `ns = && echo`도 실행된다.
    * 방법이 필요할 것 같다...
  * [출처](https://opensource.com/article/18/9/tips-productivity-zsh)
