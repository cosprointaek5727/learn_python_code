#1. if문
#영어처럼 읽기
#만약 조건이 참이라면 {} 괄호가 실행될텐데
if 조건:
  #조건이 참일 경우 실행되는 코드

#2. if-else문
#영어처럼 읽기
#만약 조건이 참이라면 {} 괄호가 실행될텐데
#그렇지 않다면 {} 괄호가 실행될텐데
if 조건:
  #조건이 참일 경우 실행되는 코드
else:
  #조건이 거짓일 경우 실행되는 코드

#3. if-else if-else문:
#영어처럼 읽기
#만약 조건1이 참이라면 {} 괄호가 실행될텐데
#그렇지 않고 만약에 조건2가 참이라면 {} 괄호가 실행될텐데
#그렇지 않다면 {} 괄호가 실행될텐데
if 조건1:
  #조건1이 참일 경우 실행되는 코드
elif 조건2:
  #조건2가 참일 경우 실행되는 코드
else:
  #모든 조건이 거짓일 경우 실행되는 코드


#조건문 예제
jeju_temperature = -1 #변수저장

if jeju_temperature == 10:
  print("야외에서 운동했을텐데")
elif jeju_temperature == -1:
  print("실내에서 운동했을텐데")
else:
  print("운동안할텐데")


#if + 입력받는 input 문 만들어보기
jeju_temperature = int(input("현재 온도를 입력해주세요!: "))

if jeju_temperature == 10:
  print("야외에서 운동했을텐데")
elif jeju_temperature == -1:
  print("실내에서 운동했을텐데")
else:
  print("운동안할텐데")


