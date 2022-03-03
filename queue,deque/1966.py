import sys
t = int(sys.stdin.readline().rstrip())
from collections import deque
for i in range(t):
    n, m = map(int,sys.stdin.readline().rstrip().split())
    val = list(map(int,sys.stdin.readline().rstrip().split()))
    val_queue = deque(val)
    index = deque([i for i in range(n)])
    cnt=0
    while True:
        if val[index[0]]==max(val_queue):
            cnt+=1
            tmp=index.popleft()
            val_queue.popleft()
            if tmp==m:
                print(cnt)
                break
        else:
            tmp=index.popleft()
            index.append(tmp)
            tmp = val_queue.popleft()
            val_queue.append(tmp)
