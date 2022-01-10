# 이진 탐색 재귀적 구현
def binary_search(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2
    # 중간점과 타겟 비교
    if array[mid]==target:
        return mid
    # 타겟이 중간점의 값보다 작은 경우
    elif array[mid]>=target:
        return binary_search(array, target, start, mid-1)
    # 타겟이 중간점의 값보다 큰 경우
    else:
        return binary_search(array, target, mid+1, end)

n, target = list(map(int,input().split()))

array = list(map(int,input().split()))

result = binary_search(array, target, 0, n-1)
if result==None:
    print("Fail to find the target")
else:
    print(result+1)

"""
bisect_left, right를 이용해
값이 특정 범위에 속하는 데이터 개수 구하기
"""

def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    return right_index - left_index

