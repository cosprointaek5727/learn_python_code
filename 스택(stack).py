#스택(stack)
#일반 명사 = (깔끔하게 정돈하여) 쌓다[포개다], 포개지다.
#LIFO = Last In First Out -> 맨 아래 접시가 아닌 다른 접시를 모두 꺼낸 뒤에 맨 아래 접시를 꺼내야 할 것입니다.
#(= LIFO= 가장 마지막에 들어온 데이터가 가장 먼저 사용된다.)
#자주 사용하는 브라우저의 히르토리 기록입니다.
#즉 가장 마지막에 쌓은 접시를 가장 먼저 꺼내게 됩니다.
#브라우저에서 뒤로가기 클릭했을 경우 가장 마지막에 방문해던 페이지로 돌아가게됩니다.

stack = []  #stack이라는 변수명의 빈리스트 생성
stack.append('a') #stack변수에 append함수를 사용해 a자료추가  -> ['a']
stack.append('b') #stack변수에 append함수를 사용해 b자료추가  -> ['a', 'b']
stack.append('c') #stack변수에 append함수를 사용해 c자료추가  -> ['a', 'b', 'c']

print(stack)  #['a', 'b', 'c']

#마지막에 추가된 요소를 사용
topElement = stack.pop()  #pop은 가장 마지막에 들어온 수를 의미함 / topElement = 'c'

print(topElement) #c
print(stack) #['a', 'b']