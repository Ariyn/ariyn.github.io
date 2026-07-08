---
layout: post
title: "맥에서 swift로 window들의 정보를 가져오는 방법"
date: "2021-08-10T23:07:05+07:00"
lastmod: "2021-12-01T22:26:33+07:00"
slug: "epmnjjhnk"
permalink: "/posts/epmnjjhnk/"
kind: dev
section: til
category: library-usage
tags:
  - "TIL"
  - "swift"
  - "osx"
---
`CGWindowListCopyWindowInfo`로 macOS의 현재 window 정보를 가져올 수 있다.
window bounds, owner process, window title 같은 값이 dictionary 형태로 반환된다.

{: .tractatus}
1. 예시는 아래와 같다.

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
             height:bound["Height"] as? Int ?? -10000
         ))
     }

     if let jsonData = try? JSONEncoder().encode(collectedInfo), let jsonString = String(data: jsonData, encoding: .utf8) {
         print(jsonString)
     }
   ```

   1. `CGWindowListCopyWindowInfo`로 macOS의 현재 window 정보를 가져올 수 있다.

   2. window bounds, owner process, window title 같은 값이 dictionary 형태로 반환된다.

   3. bounds key는 예시 출력처럼 `X`, `Y`, `Width`, `Height`를 사용한다.

   4. 이후에 환경설정 > 보안 > 화면 기록에서 터미널을 추가하고 터미널을 재시작해야 한다.

   5. 권한이 없으면 `kCGWindowName`, 즉 각 window 제목이 비어 보일 수 있다.

   6. `CGWindowListCopyWindowInfo`가 리턴하는 형식은 대략 아래와 같다.

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

   7. 추가로 할 일

   8. 아이콘 정보 가져오기

      1. https://stackoverflow.com/questions/36389173/how-to-observe-other-application-icon-in-os-x

   9. 정리하면, window 목록 자체를 가져오는 일보다 permission과 dictionary key를 정확히 확인하는 일이 더 중요했다.

   10. Swift에서 `NSDictionary`를 직접 다루면 key 오타가 런타임 기본값으로 숨어버리기 쉽다.

   11. 이런 코드는 예시 출력과 실제 접근 key를 같이 두고 확인하는 편이 안전하다.
