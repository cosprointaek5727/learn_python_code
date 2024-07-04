# 큐
# 일반 명사 = (무엇을 기다리는 사람자동차 등의) 줄
# 고유 명사 = 가장 먼저 집어 넣은 데이터가 먼저 나오는 FIFO구조로 저장하는 형식을 말합니다.
# FIFO = First In First Out -> 먼저 들어온 데이터가 먼저 나오는 것입니다.
# 즉 가장 먼저 들어온 요소가 가장 먼저 나오게 됩니다.

from queue import Queue   # Queue 모듈 추가
# 인자값으로 maxSize를 정할 수있습니다. 만약 인자값이 0 이하인 경우 큐의 크기는 무한대가 됩니다.
q = Queue()
q.put('apple')    # ['apple']
q.put('banana')   # ['apple', 'banana']
q.put('cherry')   # ['apple', 'banana', 'cherry']

#요소 제거 및 반환
print(q.queue)  #큐를 출력
print(q.get())    # 가장 먼저 큐에 들어온 'apple'을 사용하고 큐에서 지운다.
print(q.queue)    #'apple'을 사용했기 때문에 현재 큐의 값은 ['banana', 'cherry']이다.
print(q.get())    # 가장 먼저 들어온 값 'banana'를 사용하고 큐에서 지운다.
print(q.queue)    # 'banana'를 사용했기 때문에 큐에는 ['cherry']만 남아 있다.
print(q.get())    # 큐에서 가장 먼저 들어온 값 'cherry'를 사용하고 큐에서 지운다.

#큐가 비어 있는지 확인
print(q.empty())  # 출력: True 큐가다 비워졌기 때문에 True를 출력한다.