"""
#1 Factorial 이용하기
from math import factorial
N=int(input())
f=factorial(N)
cnt=0
while f%10==0:
    f=f//10
    cnt+=1
print(cnt)
"""

#2 소인수 분해 했을 때 5의 개수 구하기
N=int(input())
cnt=0
for i in range(5,N+1):
    tmp=i
    while tmp%5==0:
        tmp=tmp//5
        cnt+=1
print(cnt)
