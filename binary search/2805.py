import sys

input = sys.stdin.readline

n, m = map(int,input().rstrip().split())
tree = list(map(int, input().rstrip().split()))

left, right = 1, max(tree)
ans = 0
while left<=right:
    tmp = 0
    mid = (left+right)//2
    tmp = sum(item-mid if item>mid else 0 for item in tree)
    if tmp>=m:
        ans = max(ans, mid)
        left = mid+1
    else:
        right = mid -1
print(ans)
        
