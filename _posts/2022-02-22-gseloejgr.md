---
layout: post
title: "golang의 struct에서 멤버의 이름은 두개 이상 동시에 선언할 수 있다"
date: "2022-02-22T00:26:42+07:00"
lastmod: "2022-02-22T00:29:38+07:00"
slug: "gseloejgr"
permalink: "/posts/gseloejgr/"
kind: dev
tags:
  - "golang"
  - "TIL"
---
```go
  type foo struct {
    bar, bar2 int
  }
  
  f := foo {
    bar: 1,
    bar2: 2,
  }
  ```

  * 마치 함수 파라미터에서 두개 이상 받을 수 있는것 처럼
  * 그래서인지 ast의 Field를 보면, Names가 list로 되어있음
    ```go
    // A Field represents a Field declaration list in a struct type,
    // a method list in an interface type, or a parameter/result declaration
    // in a signature.
    // Field.Names is nil for unnamed parameters (parameter lists which only contain types)
    // and embedded struct fields. In the latter case, the field name is the type name.
    // Field.Names contains a single name "type" for elements of interface type lists.
    // Types belonging to the same type list share the same "type" identifier which also
    // records the position of that keyword.
    //
    type Field struct {
    	Doc     *CommentGroup // associated documentation; or nil
    	Names   []*Ident      // field/method/(type) parameter names, or type "type"; or nil
    	Type    Expr          // field/method/parameter type, type list type; or nil
    	Tag     *BasicLit     // field tag; or nil
    	Comment *CommentGroup // line comments; or nil
    }
    ```
