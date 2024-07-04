#연산
7 % 3
7 // 3
2 ** 3
2 == 3

#1)
sum = 0
for i in range(1, 11):
  print(i)
  sum = sum + i   #첫번째 답이 1이 나온 이유는? = sum은 0이니 0 + 1을하여 1이 나오게됨 그래서 계산 결과가 sum == 1

print(sum)

#2)
sum = 0
for i in range(1, 11):
  print(i, sum)
  sum = sum + i

print(sum)

#3)
a = 3
if a > 2:
  print("aa")

#4)
a = 3
if a != 2:
  print("aa")


#5)
a = 3
b = 4
if a > 2 and b > 3:
  print("aa")


#6)
a = [1, 2, 3, 4, 5]

3 in a


#7)
some = 1

if some == 2:
  print("정답이 아닙니다.")

elif some == 1:
  print("정답입니다.")



#8)
fruits = ["apple", "banana", "cherry", "kiwi"]
newlist = []

for fruit in fruits:
 if "a" in fruit:   #fruits의 단어들 중에서 a가 들어가 있는 것을 골라줘
  newlist.append(fruit)

print(newlist)


#9)
a = [True] * 10
print(a)


#10)
print('*' * 10)