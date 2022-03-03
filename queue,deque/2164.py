import sys
n=int(sys.stdin.readline().rstrip())

from collections import deque

queue = deque([i for i in range(1,n+1)])

for i in range(n-1):
    queue.popleft()
    tmp = queue.popleft()
    queue.append(tmp)
print(queue[0])

"""
queue = [i for i in range(1,n+1)]
for i in range(n-1):
    queue.pop(0)
    queue[0:-1], queue[-1] = queue[1:],queue[0]
print(queue[0])
"""
