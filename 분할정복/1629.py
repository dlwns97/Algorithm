import sys
input = sys.stdin.readline

a, b, c = map(int,input().rstrip().split())
"""
분배법칙을 이용한다.

(A*B)%C=(A%C)*(B%C)%C
"""

def rec(a,n):
    if n==1:
        return a%c
    else:
        tmp = rec(a,n//2)
        if n%2==0:
            return (tmp*tmp)%c
        else:
            return (tmp*tmp*a)%c
print(rec(a,b))
