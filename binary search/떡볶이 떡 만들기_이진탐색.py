# 떡볶이 떡 만들기
from bisect import bisect_right

def count_by_range(a, value):
    index = bisect_right(a,value)
    res = 0
    for i in range(index, len(a)):
        res+=(a[i]-value)
    return res

n, m = map(int,input().split())

arr = list(map(int,input().split()))
arr.sort()

flag = 1
res = 0
idx = n//2
mid = arr[idx]

while True:
    count = count_by_range(arr, mid)
    if count>=m:
        if mid<res:
            mid=res
            break
        res=mid
        mid+=1
    else:
        if res<mid and res!=0:
            mid=res
            break
        mid-=1    
print(mid)

"""
이진 탐색을 더욱 잘 활용한 풀이
"""
n, m = list(map(int,input().split(' ')))

array = list(map(int,input().split()))

start, end = (0, max(array))

# 이진 탐색 수행
result = 0
while start<=end:
    total = 0
    mid = (start+end)//2
    for x in array:
        if x>mid:
            total+= x-mid
    if total<m:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
prnit(result)
