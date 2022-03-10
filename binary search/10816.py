import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
arr = sorted(list(map(int,input().rstrip().split())))
m = int(input())
lst = list(map(int,input().rstrip().split()))

"""
시간초과 발생
def bin_search(n,f,b):
    if f>b:
        return 0
    mid = (f+b)//2
    if n==arr[mid]:
        return arr[f:b+1].count(n)
    elif n<arr[mid]:
        return bin_search(n,f,mid-1)
    else:
        return bin_search(n,mid+1,b)

for item in lst:
    print(bin_search(item,0,len(arr)-1), end=" ")
"""
count = Counter(arr)

for i in range(len(lst)):
    if lst[i] in count:
        print(count[lst[i]], end=' ')
    else:
        print(0, end=' ')
