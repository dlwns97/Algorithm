import sys

input = sys.stdin.readline

while True:
    n, *sqr = map(int,input().rstrip().split())
    if n==0:
        break
    stack, res =[], 0
    for i in range(n):
        bound = i
        while stack and stack[-1][0]>=sqr[i]:
            h, bound = stack.pop()
            tmp = h*(i-bound)
            res = max(res, tmp)
        stack.append([sqr[i],bound])
    for h, bound in stack:
        res = max(res, h*(n-bound))
    print(res)
