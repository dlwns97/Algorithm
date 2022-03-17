import heapq
import sys

input = sys.stdin.readline

n = int(input().rstrip())

"""
heapsort?

로 푸니까 시간초과 발생

"""
"""
def heapsort(heap):
    ans = []
    for i in range(len(heap)):
        ans.append(heapq.heappop(heap))
    return ans
l = 0
h = []
for i in range(n):
    cmd = int(input())
    l+=1
    heapq.heappush(h, cmd)
    tmp = []
    tmp.extend(h)
    arr = heapsort(tmp)
    if l%2==1:
        print(arr[l//2])
    else:
        print(arr[l//2-1] if arr[l//2-1]<arr[l//2] else arr[l//2])
    
"""

"""
2 개의 힙을 이용하여 중간 값을 찾아낸다.

왼쪽 힙에는 최대 힙을 오른쪽 힙에는 최소 힙을 구현한다.
"""

l, r = [], []

for i in range(n):
    cmd = int(input())
    if i%2==0:
        heapq.heappush(l, -cmd)
    else:
        heapq.heappush(r, cmd)
    if i%2==1 and l[0]*(-1)>r[0]:
        a = heapq.heappop(l)*(-1)
        b = heapq.heappop(r)

        heapq.heappush(l, b*(-1))
        heapq.heappush(r, a)
    print(l[0]*(-1))
    
