#딕셔너리
#하나의 키에 하나의 벨류가 들어간다.
#딕셔너리의 경우 키값만 알고 있으면 키안에 들어 있는 벨류를 빠른 속도로 출력 가능하다.
my_dict = {'key1':'value1', 'key2':'value2', 'key3':'value3'}

print(my_dict['key1'])  #value1 출력
print(my_dict['key2'])  #value2 출력
print(my_dict['key3'])  #value3 출력

#딕셔너리 값 변경
my_dict = {'key1':'value1', 'key2':'value2', 'key3':'value3'}

my_dict['key1'] = 'new value'

print(my_dict['key1'])    #new value 출력
#키값은 변경하지 않고 벨류 값을 변경하면 출력시 변경되어 출력됨

#딕셔너리 키, 값, 쌍 삭제
my_dict = {'key1':'value1', 'key2':'value2', 'key3':'value3'}

del my_dict['key1']
print(my_dict)  #{'key2':'value2', 'key3':'value3'} 출력

my_dict.pop('key2')
print(my_dict)   #{'key3' : 'value3'} 출력

#모든 키, 값, 쌍 얻기
my_dict = {'key1':'value1', 'key2':'value2', 'key3':'value3'}
print(my_dict.items())

#모든 키 얻기
my_dict = {'key1':'value1', 'key2':'value2', 'key3':'value3'}
print(my_dict.keys())

#딕셔너리 비우기
my_dict = {'key1':'value1', 'key2':'value2', 'key3':'value3'}
my_dict.clear()
print(my_dict)  #모두 비워진 상태라 {}만 출력됨

#딕셔너리 실습
to_be = {'토익':'700점 이상', '자격증':'실기+필기'}
print(to_be.ㅏkeys())
to_be = {'토익':'700점 이상', '자격증':'필기+스피킹'}
print(to_be.values())