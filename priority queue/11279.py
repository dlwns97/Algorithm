import sys

input = sys.stdin.readline


def heapinsert(heap, x):
    h=len(heap)
    heap.append(x)
    tmp = h

    while tmp//2>0:
        if heap[tmp//2]<heap[tmp]:
            heap[tmp//2],heap[tmp] = heap[tmp],heap[tmp//2]
            tmp=tmp//2
        else:
            break

def heapremove(heap):
    if len(heap)==1:
        return 0
    heap[1],heap[-1] = heap[-1],heap[1]
    res = heap.pop()
    maxheapify(1)
    return res

def maxheapify(i):
    left = i*2
    right = i*2+1
    maxi = i

    if left<len(heap) and heap[left]>heap[maxi]:
        maxi = left
    if right<len(heap) and heap[right]>heap[maxi]:
        maxi = right
    if maxi!=i:
        heap[maxi],heap[i] = heap[i],heap[maxi]
        maxheapify(maxi)
        
n = int(input())

heap = [0]
for i in range(n):
    cmd = int(input().rstrip())
    if cmd==0:
        print(heapremove(heap))
    else:
        heapinsert(heap,cmd)


"""
heapq 라이브러리 이용

시간 초과 발생
"""
import heapq

heap = []

n = int(input())
for _ in range(n):
    cmd = int(input().rstrip())
    if cmd==0:
        if len(heap)!=0:
            print(heapq.heappop(heap)[1])
        else:
            print(0)
    else:
        heapq.heappush(heap,(-cmd, cmd))
