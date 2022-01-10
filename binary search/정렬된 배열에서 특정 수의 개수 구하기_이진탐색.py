# 정렬된 배열에서 특정 수의 개수 구하기
from bisect import bisect_right, bisect_left
import time

n, x = map(int, input().split())
array = list(map(int,input().split()))
def count_by_range(arr, left_value, right_value):
    left_index = bisect_left(arr, left_value)
    right_index = bisect_right(arr, right_value)
    return right_index - left_index
start = time.time()
res = count_by_range(array,x,x)
end = time.time()
print(res)
print(end-start)
