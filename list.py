#리스트는 왜 사용하는가?
#카테고리가 비슷한 데이터를 하나의 변수에 저장하기 위해서 사용

#리스트명 = [요소1, 요소2, 요소3,...]
음료수냉장고 = [] #빈 리스트 공간 확보

#음료수 추가
#append는 리스트 맨 뒤에 값을 붙이는 메서드
음료수냉장고.append("콜라")
음료수냉장고.append("사이다")

#다른 리스트 추가
#extend는 리스트 맨 뒤에 리스트를 추가합니다.
추가냉장고 = ["오랜지주스","사이다","오렌지주스"]
음료수냉장고.extend(추가냉장고)

#음료수 개수 확인
#리스트의 길이를확인하기 위해서 len()을 사용한다.
#len은 length의 줄임말
음료수개수 = len(음료수냉장고)
print('dmafytnrotn: ', 음료수개수)

#음료수 조회
#리스트의 주소값은 0부터 시작한다.
print("첫 번째 음료수: ", 음료수냉장고[0])
print("두 번째 음료수: ", 음료수냉장고[1])
print("세 번째 음료수: ", 음료수냉장고[2])

#음료수에 몇 개의 사이다 음료가 있는지 확인
#특정 데이터릐 개수를 추출하고 싶으면 count()를 사용한다.
print("사이다는 몇개일까요?", 음료수냉장고.count("사이다"), "개")

print(음료수냉장고)
#리스트 요소 오름차순 정렬
#sort()가 리스트를 오름차순으로 정렬해 줌.
음료수냉장고.sort()
print(음료수냉장고)

#리스트 요소 내림차순 정렬
#리스트를 내림차순 하려면 sort의 소괄호 안에 reverse=True 옵션을 넣어준다.
음료수냉장고.sort(reverse=True)
print(음료수냉장고)

#리스트 뒤집기
#리스트 안의 데이터의 순서를 뒤집고 싶을 땐 reverse()를 사용한다.
음료수냉장고.reverse()
print(음료수냉장고)

#음료수 리스트 비우는 메서드
음료수냉장고.clear()
음료수냉장고 = []


#리스트 실습
숫자칸 = [0,3,4,6,2,1,4,7]

#리스트요소 오름차순 정렬
숫자칸.sort()
print(숫자칸)

#리스트요소 내림차순 정렬
숫자칸.sort(reverse=True)
print(숫자칸)

#리스트 뒤집기
숫자칸.reverse()
print(숫자칸)

#숫자칸 리스트 비우기
#1)
숫자칸.clear()
print(숫자칸)
#2)
숫자칸=[]
print(숫자칸)

