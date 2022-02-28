# python에서 시간 제한이 0.5초 이내인 경우에
# input을 사용하면 통과할 수 없음
# 반드시 sys.stdin.readline()을 사용 

import sys
N=int(sys.stdin.readline())
stack = [0]*10000
top=0

for i in range(N):
    s=sys.stdin.readline().split()
    if s[0]=='push':
        stack[top]=int(s[1])
        top+=1
    elif s[0]=='pop':
        if top==0:
            print(-1)
        else:
            print(stack[top-1])
            top-=1
    elif s[0]=='size':
        print(top)
    elif s[0]=='empty':
        print(1 if top==0 else 0)
    else:
        print(-1 if top==0 else stack[top-1])
