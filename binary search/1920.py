import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().rstrip().split()))
m = int(input())
lst = list(map(int,input().rstrip().split()))

"""
for item in lst:
    print(1 if item in arr else 0)
이렇게 하면 시간 초과가 뜸
아마 O(n)이라서 그런거 같음
"""


arr.sort()
def bin_search(n,f,b):
    if f>b:
        return 0
    mid = (f+b)//2
    if n==arr[mid]:
        return 1
    elif n<arr[mid]:
        return bin_search(n,f,mid-1)
    else:
        return bin_search(n,mid+1,b)
for item in lst:
    print(bin_search(item,0,len(arr)-1))
    
