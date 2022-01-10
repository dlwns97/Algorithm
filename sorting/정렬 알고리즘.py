"""
정렬 알고리즘, 데이터를 기준에 따라 순서대로 나열

선택 정렬, 삽입 정렬, 퀵 정렬, 계수 정렬
"""

#1 selection sort

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i
    # 최소 인덱스 찾기
    for j in range(i, len(array)):
        if array[j]<array[min_index]:
            min_index=j
    # Swapping
    array[i],array[min_index] = array[min_index], array[i]
print(array)


# insertion sort

array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(1, len(array)):
    for j in range(i, 0, -1):
        if array[j] < array[j-1]:
            array[j], array[j-1] = array[j-1], array[j]
        else:
            break
print(array)


# quick sort

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array, start, end):
    if start>=end: # 원소가 한 개인 경우
        return
    pivot = start
    left = start+1
    right = end
    while(left<=right):
        # 피벗보다 큰 데이터를 찾을 때 까지
        while(left<=end and array[left]<=array[pivot]):
            left+=1
        # 피벗보다 작은 데이터를 찾을 때 까지
        while(right > start and array[right]>=array[pivot]):
            right-=1
        # left와 right가 엇갈리면 피벗을 교체하고 그만
        if left>right:
            array[right], array[pivot] = array[pivot], array[right]
        else:
            array[right], array[left] = array[left], array[right]
    # right가 현재 pivot의 위치임
    """재귀"""
    # 분할 이후 피벗 기준 왼쪽에서 퀵 정렬
    quick_sort(array, start, right-1)
    # 분할 이후 피벗 기준 오른쪽에서 퀵 정렬
    quick_sort(array, right+1, end)
quick_sort(array, 0, len(array)-1)
print(array)
    
# quick_sort python version

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick(array):
    # 원소가 한 개인 경우
    if len(array)<=1:
        return array
    pivot = array[0]
    tail = array[1:]

    left_side = [x for x in tail if x<pivot]
    right_side = [x for x in tail if x>pivot]

    """재귀"""
    return quick(left_side)+[pivot]+quick(right_side)
print(quick(array))


# counting sort

# 모든 원소의 값이 0보다 크거나 같다고 가정
array = [7, 7, 1, 4, 5, 3, 8, 6, 2, 2, 4, 8, 0, 2, 9]
# 모든 범위를 포함하는 리스트 선언 모든 값은 0으로 초기화
count = [0]*(max(array)+1)

for i in range(len(array)):
    count[array[i]]+=1
for i in range(len(count)):
    for j in range(count[i]):
        print(i, end=' ')

