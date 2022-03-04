import sys
from collections import deque
n, m = map(int, sys.stdin.readline().rstrip().split())

lst = deque([i for i in range(1,n+1)])
val = deque(list(map(int, sys.stdin.readline().rstrip().split())))
cnt = 0
for i in range(m):
    # 첫 번째 원소라면
    if val[i]==lst[0]:
        lst.popleft()
        continue
    if lst.index(val[i])<len(lst)/2:
        while lst[0] != val[i]:
            lst.append(lst.popleft())
            cnt+=1
        lst.popleft()
    else:
        while lst[0] != val[i]:
            lst.appendleft(lst.pop())
            cnt+=1
        lst.popleft()
print(cnt)
