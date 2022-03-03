import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
que = deque([])
for i in range(n):
    cmd = sys.stdin.readline().rstrip().split()
    if cmd[0]=='push_front':
        que.insert(0,int(cmd[1]))
    elif cmd[0]=='push_back':
        que.append(int(cmd[1]))
    elif cmd[0]=='pop_front':
        print(-1 if len(que)==0 else que.popleft())
    elif cmd[0]=='pop_back':
        print(-1 if len(que)==0 else que.pop())
    elif cmd[0]=='size':
        print(len(que))
    elif cmd[0]=='empty':
        print(1 if len(que)==0 else 0)
    elif cmd[0]=='front':
        print(-1 if len(que)==0 else que[0])
    else:
        print(-1 if len(que)==0 else que[-1])
