import sys

input = sys.stdin.readline

n, k = map(int,input().rstrip().split())

lan = [0 for _ in range(n)]
for i in range(n):
    lan[i] = int(input())
ans = -1
def func(goal, left, right):
    global ans
    if left>right:
        return
    tmp = 0
    mid = (left+right)//2
    for i in range(len(lan)):
        tmp+=lan[i]//mid
    if tmp>=goal:
        ans = max(ans, mid)
        return func(goal, mid+1, right)
    else:
        return func(goal, left, mid-1)
func(k, 1, max(lan))
print(ans)
        
