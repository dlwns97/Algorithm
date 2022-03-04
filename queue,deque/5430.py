import sys
from collections import deque
input = sys.stdin.readline

T = int(input())

for i in range(T):
    cmd = input().rstrip()
    n = int(input())
    lst = deque(input().rstrip()[1:-1].split(","))
    if n==0:
        lst = deque()

    flag, r = 0, 0 # flag, reverse num
    for c in cmd:
        if c=='R':
            r+=1
        elif c=='D':
            if len(lst)==0:
                flag=1
                print('error')
                break
            else:
                if r%2==0:
                    lst.popleft()
                else:
                    lst.pop()
    if flag==0:
        if r%2==0:
            print('['+','.join(lst)+']')
        else:
            lst.reverse()
            print('['+','.join(lst)+']')
