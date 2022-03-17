# minheap

import sys

input = sys.stdin.readline

# 1.

class MinHeap:
    def __init__(self):
        self.heap = [0]
    def insert(self, x):
        self.heap.append(x)
        idx = len(self.heap)-1
        while idx//2>0:
            if self.heap[idx]<self.heap[idx//2]:
                self.heap[idx], self.heap[idx//2] = self.heap[idx//2], self.heap[idx]
                idx = idx//2
            else:
                break
    def remove(self):
        if len(self.heap)==1:
            return (0,0)
        self.heap[-1], self.heap[1] = self.heap[1], self.heap[-1]
        ans = self.heap.pop()
        self.heapify(1)
        return ans
    def heapify(self, i):
        mini = i
        l, r = i*2, i*2+1
        if l<len(self.heap) and self.heap[l]<self.heap[mini]:
            mini=l
        if r<len(self.heap) and self.heap[r]<self.heap[mini]:
            mini = r
        if i!=mini:
            self.heap[i], self.heap[mini] = self.heap[mini], self.heap[i]
            self.heapify(mini)

n = int(input())
h = MinHeap()

for i in range(n):
    cmd = int(input().rstrip())
    if cmd == 0:
        print(h.remove()[1])
    else:
        if cmd<0:
            h.insert((-cmd,cmd))
        else:
            h.insert((cmd,cmd))

# 2.

import heapq

h = []

n = int(input())
for i in range(n):
    cmd = int(input().rstrip())
    if cmd==0:
        if len(h)!=0:
            print(heapq.heappop(h)[1])
        else:
            print(0)
    else:
        if cmd<0:
            heapq.heappush(h, (-cmd, cmd))
        else:
            heapq.heappush(h, (cmd, cmd))
