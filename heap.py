# 힙(heap)
# 일반 명사 = (아무렇게나 쌓아 놓은) 더미[무더기]
# 고유명사 = 우선 순위 큐를 위해 만들어진 자료구조. 우선순위가 존재하며, 가장 우선순위가 높은 데이터가 먼저 나간다.

import heapq    # 내장 라이브러리 추가

heap = []   # 힙으로 이용할 리스트 생성


# 힙에 데이터 추가하기
heapq.heappush(heap, 5)   # [5]
heapq.heappush(heap, 3)   # [3, 5] / 힙 속성의 최소 힙이기 때문에, 작은 숫자가 더 앞으로 와야합니다.
heapq.heappush(heap, 7)   # [3, 5, 7]
heapq.heappush(heap, 1)   # [1, 3, 5, 7]


# 힙 꺼내기
# -> 힙의 가장 작은 요소를 제거하고 반환합니다.
small = heapq.heappop(heap)
print("heap에서 small 변수로 꺼낸 값: ", small)   # small = 1
print("small 변수로 가장 작은 값을 꺼내주고 난 뒤의 heap의 값: ", heap)    # heap = [3, 5, 7]

small_next = heapq.heappop(heap)
print("heap에서 small_next 변수로 꺼낸 값: ", small_next)    # small_next = 3
print("small_next 변수로 가장 작은 값을 꺼내주고 난 뒤의 heap의 값: ", heap)    # heap = [5, 7]


# 가장 작은 요소 n개 꺼내기
# ->힙의 가장 작은 요소를 n개 꺼내옵니다. 이는 제거하는 것이 아니라 단순히 값을 참조합니다.
heap2 = [1, 3, 5, 7, 9, 10, 11, 20]
smallHeap = heapq.nsmallest(3, heap2)
print("heap2에서 smallHeap 변수로 가장 작은 순서대로 3개까지 참조하여 가져온 값: ", smallHeap)
print("heap2의 현재 값: ", heap2)

# 가장 큰 요소 n개 꺼내기
# -> 힙의 가장 큰 요소를 n개 꺼내옵니다. 이는 제거하는 것이 아니라 단순히 값을 참조합니다.

largeHeap = heapq.nlargest(3, heap2)
print("heap2에서 largeHeap 변수로 가장 큰 순서대로 3개까지 참좋하여 가져온 값: ", largeHeap)
print("heap2의 현재 값: ", heap2)


# k번째로 작은 요소 찾기
# 주어진 리스트에서 k번째로 작은 요소 찾는 함수를 구현하세요.
# 단, 리스트의 길이는 k 이상이라고 가정
# (예: [10, 5, 3, 7, 8], k = 3 일 때, 3번째로 작은 요소인 7을 반환해야 합니다.)

'''
#작은 수 2개 꺼내기
import heapq
heap = [11, 2, 3, 5, 6]
smallest = heapq.nsmallest(2, heap)
print("heap에서 smallest 변수로 가장 작은 순서대로 3개까지 참조하여 가져온 값: ", smallest)
'''

# k번째 숫자 꺼내기

def find_kth_smallest(nums, k):
  heap = []   # 힙으로 사용할 리스트를 선언합니다.
  for num in nums:
    heapq.heappush(heap, num)   # nums로 들어온 배열을 모두 돌면서 heapq를 사용해 추가해 줍니다.

# 가장 작은 요소를 k개 만큼 꺼내서 리스트를 생성합니다.
# 이렇게 구현하게 되면 smallest에는 길이가 k인 숫자의 리스트가 생성됩니다.
  smallest = heap.nsmallest(k, heap)
# 길이가 k인 숫자 리스트에서 가장 마지막 인데스가 우리가 원하는 값인 k번째
# 작은 수 이기에 -1을 사용해 가장 마지막 인데스를 참조 합니다.
  redturn smallesr[-1]

num = [10, 5, 3, 7, 8]
k = 3
print(find_kth_smallest(num, k))    # 7출력