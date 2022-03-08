import sys
#import numpy

input = sys.stdin.readline
"""
n,m = map(int,input().rstrip().split())
A = []
for i in range(n):
    tmp = list(map(int,input().rstrip().split()))
    A.append(tmp)
m,k = map(int,input().rstrip().split())
B = []
for i in range(m):
    tmp = list(map(int,input().rstrip().split()))
    B.append(tmp)

res = numpy.matmul(A,B)

for item in res:
    for val in item:
        print(val, end=" ")
    print()
"""

"""
백준에서는 numpy 모듈을 사용할 수 없음

행렬 곱을 분할 정복으로 해결하는 방법은?

"""
n,m = map(int,input().rstrip().split())
A = []
for i in range(n):
    tmp = list(map(int,input().rstrip().split()))
    A.append(tmp)
m,k = map(int,input().rstrip().split())
B = []
for i in range(m):
    tmp = list(map(int,input().rstrip().split()))
    B.append(tmp)

for i in range(n):
    for j in range(k):
        tmp=0
        for l in range(m):
            tmp+=A[i][l]*B[l][j]
        print(tmp, end=" ")
    print()
