#실습
print("오늘은 학교에서 코딩 기본반 수업이 있는 날이다.")
print("수업 시작 시간은 오전 10시이다.")
print("현재 시간은오전 9시 그런데 배가 고프다..")
print("어떻게 하지...?")
print("1. 밥을 먹고 간다.   2. 밥을 먹지않고 학교에 간다.")

selection = int(input("1번과 2번 중에 고르세요."))
if selection == 1: #1번째 질문 밥 먹고간다.
  print("밥먹고 학교 가야겠다~")
  print("그런데 뭘 먹고 가지?")
  print("1. 집밥  2. 샌드위치 3. 샐러드")

  selection = int(input("어떤걸 먹을까나?"))
  if selection == 1: #1-1 질문에 집밥
    print("집밥을 먹기로 했다.")
    print("집밥을 먹으려고 밥솥을 열었는데 밥이 없다...")
    print("배고픈데 어떻게하지?")
    print("1. 밥을 새로한다.  2. 시리얼을 먹는다. 3. 시간이 없다 그냥 학교로 간다...") #1-2 질문

    selection = int(input("어떻게할지 선택해보자!")) #1-2 질문 밥새로, 시리얼, 그냥 학교로
    if selection == 1: #1-2 밥 새로
      print("밥을 새로 했는데 밥이 완성되는 9시50분이 되었다.")
      print("망했다... 학교로 달려간다.")
    elif selection ==2: #1-2 시리얼
      print("바삭바삭 시리얼을 먹었다.")
      print("든든하게 학교로 갈 수 있었다.")
    elif selection ==3: #1-2 그냥 학교
      print("학교로 향하는 배고픈 그의 뒷모습이 보였다...")
    else:
      print("고민하다 시간이 다 지나버렸다 학교로 달려간다.")

  elif selection == 2: #1-1 질문 샌드위치
    print("샌드위치를 먹기로 했다.")
    print("1. 스타벅스 샌드위치를 먹을까?")
    print("2. 파리바게트 샌드위치를 먹을까?")

    selection = int(input("브랜드를 고민해볼까?"))
    if selection == 1 : #1-1 질문의 브랜드 샌드위치 스타벅스
      print("스타벅스에 도착했다.")
      print("무슨 샌드위치를 먹을까?")
      print("1. 토마토 치즈 베이글  2. 크림치즈 베이글")

      selection = int(input("2개중에서 골라야징"))
      if selection == 1 :
        print("토마토 치즈 베이글로 주시는데 따뜻하게 데워주세요!")
        print("샌드위치를 먹으며 학교에 갔다.")
      elif selection == 2:
        print("크림치즈 베이글로 주시는데 나이프도 같이 주시겠어요?")
        print("샌드위치를 먹으며 학교에 갔다.")
      else:
        print("다시 골라보자")

    elif selection == 2 : #1-1 질문의 브랜드 샌드위치 파리바게트
      print("파리바게트에 도착했다.")
      print("아싸! 운좋게 마지막 하나 남은 BLT 샌드위치를 구매했다! 완전 러키비키잖아~?!")
      print("샌드위치를 먹으며 학교에 갔다.")
    else :
      print("다시골라보자!")

  elif selection == 3: #1-1 질문 샐러드
    print("샐러드를 먹기로 했다.")
    print("엄마가 물어보셨다.")
    print("샐러드에 치킨텐더 넣어줄까? 라고")
    print("샐러드에 치킨 텐더를 넣어야 할까 말아야할까 고민된다.")
    print("1. 넣는다  2. 안넣는다.")

    selection =int(input("선택해주세요."))
    if selection == 1:
      print("네 엄마 넣어주세요!")
      print("엄마가 준비해준 치킨텐더 샐러드를 먹고 학교에 갔다.")
    elif selection == 2:
      print("아뇨 괜찮아요 엄마.")
      print("엄마가 준비해준 베지샐러드를 먹고 학교에 갔다.")
    else:
      print("다시 생각해보자!")

  else:
    print("다시 골라보자!")

elif selection == 2: #1번째 질문 밥 안먹고 학교간다.
  print("꼬르륵... 터덜터덜 그렇게 학교에 도착하였다.")
else:
  print("다시 생각해보자!")