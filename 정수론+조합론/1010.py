from math import factorial
T=int(input())

for i in range(T):
    a, b = map(int,input().split())
    if a>b:
        a, b = b, a
    print(factorial(b)//(factorial(a)*factorial(b-a)))
