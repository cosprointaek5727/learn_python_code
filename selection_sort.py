def selectionSort(arr, start):    # 선택 정렬 함수를 정의합니다. 이 함수는 재귀적으로 동작합니다.
  if start < len(arr) - 1:
  # 'start'가 배열 길이보다 작은 경우에만 동작합니다.
  # 'start'는 정렬이 완료된 배열 부분의 바로 다음 인덱스를 가리킵니다.
    minIndex = start    # 가장 작은 요소의 인덱스를 추적하는 변수를 설정합니다. 초기값은 'start'로 설정합니다.

    for i in range(start, len(arr)):    # 시작 위치부터 배열의 끝까지 모든 요소를 순회합니다. 0~6[0,1,2,3,4,5,6]
      if arr[i] < arr[minIndex]:
      # 만약 현재 요소가 현재 최소 요소보다 작다면,
      # 최소 요소의 인덱스를 현재 요소의 인덱스로 업데이트합니다.
        minIndex = i

    arr[start], arr[minIndex] = arr[minIndex], arr[start]   # 시작 위치의 요소와 가장 작은 요소를 교환합니다.

    selectionSort(arr, start + 1)
    # 배열의 다음 부분에 대해 선택 정렬을 수행합니다.
    # 이는 'start' 인덱스를 1씩 증가시키면서 재귀적으로 함수를 호출함으로써 수행됩니다.

numbers = [64, 34, 25, 12, 22, 11, 90]    # 정렬할 숫자들을 포함하는 리스트를 정의합니다.
selectionSort(numbers, 0)   # 정의된 리스트에 선택 정렬 함수를 적용합니다. 처음 시작 인덱스는 0부터 시작입니다.

print(numbers)    # 정렬된 리스트를 출력합니다.