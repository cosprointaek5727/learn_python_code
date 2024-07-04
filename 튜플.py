#튜플
#절대 변하지 않는 불변의 값을 사용
#리스트는 []를 사용하지만, 튜플은 ()를 사용한다.
#튜플은 () 없이도 생성 가능함

#튜플 생성
my_tuple = (1, 2, 3)
print(my_tuple)

#튜플은 소괄호() 없이도 생성 가능
my_tuple = 1, 2, 3
print(my_tuple)


#튜플 값 가져오기
my_tuple = (1, 2, 3)

print(my_tuple[1]) #2출력
print(my_tuple[-1])  #3출력


#튜플 자르기 (슬라이싱)
my_tuple = (1, 2, 3)
print(my_tuple[1:2])  #2 출력


#튜플 값 한번에 변수에 할당하기(언 패킹)

my_tuple = (1, 2, 3)

a, b, c = my_tuple

print(a)
print(b)
print(c)

#한번에 할당하는 방법
my_tuple = (1,2,3,4,5,6,7,8,9,10)
a, b, c = my_tuple

print(a)
print(b)
print(c)