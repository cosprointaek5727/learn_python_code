#재귀 함수
#일반 명사 -> 재귀: 원래의 자리로 되돌아가거나 되돌아옴
#고유명사 -> 재귀: 주어진 문제를 해결하기위하여 하나의 함수에서 자신을 다시 호출하여 작업을수행하는 방식

#재귀함수란?
#= "자기 자신을 호출하는 함수"라고 설명할 수 있습니다.
#호출하는 함수 내부에서 원하는 결과 값이 나올 때까지 같은 함수를 반복하여 부르는 행위를 의미합니다.

#왜 사용 할까?
#= 재귀 함수가 아닌 방식으로 문제를 충분히 해결할 수 있습니다.
#다만 재귀적으로 문제를 접근하면 더 간단히 해결할 수 있고 코드가 더욱 간결해지고 이해하기 쉬운 경우가 많습니다.

#카운트 다운 함수
def countdown(number):
  print(number, "!!")

countdown(3)
countdown(2)
countdown(1)
countdown("발사!")

#for문 이용 카운트다운 코드
def countdown(number):
  print(number, "!!")   # 각 점수마다 !!도 붙어서 출력

for i in range(10, 0, -1):    # 10부터 0까지 -1씩 줄어들면서 발사까지 출력
  countdown(i)

countdown("발사")


#위 코드를 재귀 함수로 변경하는 코드
def countdown(n):
  if n == 0:
    print("발사")
  else:
    print(n, "!!")
    countdown(n-1)    #자기 자신을 호출

countdown(10)