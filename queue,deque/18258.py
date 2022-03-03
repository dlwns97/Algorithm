import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())

queue = deque([])
for i in range(n):
    cmd = sys.stdin.readline().rstrip().split()

    if cmd[0]=='push':
        queue.append(int(cmd[1]))
    elif cmd[0]=='pop':
        if len(queue)==0:
            print(-1)
        else:
            print(queue.popleft())
    elif cmd[0]=='size':
        print(len(queue))
    elif cmd[0]=='empty':
        print(1 if len(queue)==0 else 0)
    elif cmd[0]=='front':
        if len(queue)==0:
            print(-1)
        else:
            print(queue[0])
    else:
        if len(queue)==0:
            print(-1)
        else:
            print(queue[-1])
