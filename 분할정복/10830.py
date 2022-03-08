import sys

input = sys.stdin.readline

n, b = map(int,input().rstrip().split())
a=[]
for i in range(n):
    a.append(list(map(int,input().rstrip().split())))


def matmul(a, b):
    s=len(a)
    res=[[0 for _ in range(s)] for _ in range(s)]
    for i in range(s):
        for j in range(s):
            for k in range(s):
                res[i][j] += a[i][k]*b[k][j]
            res[i][j]=res[i][j]%1000
    return res

def rec(a, n):
    if n==1:
        for i in range(len(a)):
            for j in range(len(a)):
                a[i][j] = a[i][j]%1000
        return a
    elif n==2:
        return matmul(a, a)
    tmp = rec(a,n//2)
    if n%2==0:
        return matmul(tmp, tmp)
    else:
        return matmul(matmul(tmp, tmp), a)

res = rec(a,b)
for item in res:
    print(*item)
    
