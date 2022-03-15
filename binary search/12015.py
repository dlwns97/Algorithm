import sys

input = sys.stdin.readline

n = int(input())
lst = map(int,input().rstrip().split())

# 무엇을 기준으로 이분 탐색을 할 것인지.

"""
LIS는 이중 포문을 통해 구할 수 있다.

이 때, 두 번째 포문을 이분 탐색으로 대체하여 효율성을 찾는다.
"""

def binsearch(x):
    l, r = 1, len(lis)-1
    while l<r:
        m = (l+r)//2
        if lis[m]<x:
            l=m+1
        elif lis[m]>x:
            r=m
        else:
            l=r=m
    return r
lis = [0]
for item in lst:
    if item>lis[-1]:
        lis.append(item)
    else:
        lis[binsearch(item)]=item
print(len(lis)-1)
