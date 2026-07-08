---
layout: post
title: "맥에서 swift로 window들의 정보를 가져오는 방법"
date: "2021-08-10T23:07:05+07:00"
lastmod: "2021-12-01T22:26:33+07:00"
slug: "epmnjjhnk"
permalink: "/posts/epmnjjhnk/"
kind: dev
tags:
  - "TIL"
  - "swift"
  - "osx"
---
```swift
  import Cocoa
  import Quartz
  
  let options:CGWindowListOption = CGWindowListOption(arrayLiteral: CGWindowListOption.excludeDesktopElements, CGWindowListOption.optionOnScreenOnly)
  let relativeToWindow: CGWindowID = kCGNullWindowID
  
  let infos = CGWindowListCopyWindowInfo(options, relativeToWindow)
  
  struct WindowData:Codable {
      let processName: String
      let windowName: String
      let x: Int
      let y: Int
      let width: Int
      let height: Int
  }
  var collectedInfo: [WindowData] = []
  for info in infos as! [NSDictionary] {
      let bound:NSDictionary = info["kCGWindowBounds"] as! NSDictionary
      let processName:String = info["kCGWindowOwnerName"] as? String ?? ""
      let windowName:String = info["kCGWindowName"] as? String ?? ""
  
      collectedInfo.append(WindowData(
          processName: processName.replacingOccurrences(of: ",", with:"\\,"),
          windowName: windowName.replacingOccurrences(of: ",", with:"\\,"),
          x:bound["X"] as? Int ?? -10000,
          y:bound["Y"] as? Int ?? -10000,
          width:bound["width"] as? Int ?? -10000,
          height:bound["hwight"] as? Int ?? -10000
      ))
  }
  
  if let jsonData = try? JSONEncoder().encode(collectedInfo), let jsonString = String(data: jsonData, encoding: .utf8) {
      print(jsonString)
  }
  ```

  * 이후에 환경설정 > 보안 > 화면 기록에서 터미널을 추가 & 터미널 재시작 해줘야 한다.
    * 안할경우 kCGWindowName (각 위도우별 제목)이 안뜸
  * CGWindowListCopyWindowInfo가 리턴하는 형식
    ```swift
    [
      {
        kCGWindowAlpha = 0;
        kCGWindowBounds =     {
            Height = 0;
            Width = 0;
            X = 0;
            Y = 0;
        };
        kCGWindowIsOnscreen = 0;
        kCGWindowLayer = 0;
        kCGWindowMemoryUsage = 1232;
        kCGWindowName = "utf-8 encoded string";
        kCGWindowNumber = 1884;
        kCGWindowOwnerName = "utf-8 encoded string";
        kCGWindowOwnerPID = 2895;
        kCGWindowSharingState = 1;
        kCGWindowStoreType = 1;
    }
    ]
    ```

  * 추가적으로 할 일
    * 아이콘 정보 가져오기
      * https://stackoverflow.com/questions/36389173/how-to-observe-other-application-icon-in-os-x
  * 느낀점
    * 윈도우의 정보를 가져오도록 구현하는것과 비슷한 시간이 걸린 json serialize
    * 이렇게 어려울 일인가? 으음....
    * 내가 swift의 핵심을 이해 못하는건가, swift의 핵심이 맛이 가 있는것인가...
