# 파이썬 변수 선언하는 예제
# 파이썬은 변수를 변수명 = 값; 으로 선언할 수 있다.

#파이썬 정수(소숫점x)
age = 22 # age(나이)변수에 정수값 22를 저장합니다.
year = 2024 # 년도(year)변수에 정수값 2024를 저장합니다.
#자바 정수
int age = 22;
year = 2024;

#파이썬 실수(=소숫점ㅇ)
temperature = 36.5 # temperature 변수에 실수값 36.5를 저장합니다.
price = 9.99 # price 변수에 실수값 9.99를 저장합니다.
#자바 실수
float temperature = 36.5;
float price = 9.99;

#파이썬 문자와 문자열
#문자는 = 'ㄱ', 'ㄴ', 'ㄷ'
#문자열 = 'ㄱㄴㄷ', '가나다', '안녕'
name = "John" # name변수에 john이라는  문자열을 저장합니다.
message = "siri!" # message변수에 siri!라는 문자열을 저장합니다.
만나서_반가워 = "hello, bitch!" #만나서_반가워 라는 변수에 hello, bitch! 라는 문자열을 저장합니다.
모기 = "ㅗ" # 모기라는 변수에 ㅗ라는 문자를 저장합니다.
#자바 문자와 문자열
string name = "John";
string message = "siri!";

#파이썬 논리 (앞글자는 꼭 대문자로 적어야함)
is_valid = True # is_valid 변수에 True라는 논리형을 저장합니다.
is_found = False # is_found변수에 Found라는 논리형을 저장합니다.
#자바 논리
boolean is_valid = True
boolean is_found = False



#파이썬 입력(input)과 출력(print)
 #input()
 #input("유저에게 입력 요청시 보여주고 싶은 메세지를 여기에 적습니다")
# 프로그램에서 사용자가 입력하도록 하는 코드
#input()으로 콘솔에서 사용자에게 데이터를 입력 받을 수 있다.
#input()의 소괄호 안에 사용자에게 어떤 데이터를 입력해야할지 알려주는 문구를 작성한다.
name = input("이름을 입력하세요: ")
age = int(input("나이를 입력하세요: ")) #어떠한 정수값을 받을 때는 input앞에 int를넣어야 숫자로 인식됨 / 안넣으면 문자열로 인식됨

#프로그램에서 출력하는 코드
#print()로 콘솔(=실행시키는 창)에 출력을 해줄 수 있다.
#print()의 소괄호 안에 출력할 데이터를 넣어준다.
print("입력받은 이름:", name)
print("입력받은 나이:", age)


# 응용하여 만들어보기
city = input("살고있는 도시를 적어주세요: ")
year = int(input("몇년동안 살았나요?: "))

print("입력받은 도시:", city)
print("입력받은 년도:", year, str("년"))


