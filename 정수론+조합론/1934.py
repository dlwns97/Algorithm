T=int(input())

def gcd(a, b):
    if a>b:
        a, b = b, a

    for i in range(a, 0, -1):
        if a%i==0 and b%i==0:
            break
    return i

for i in range(T):
    a, b = map(int,input().split())
    g = gcd(a,b)
    L = (a*b)//g
    print(L)

# 유클리드 알고리즘으로 최대공약수 구하기

for i in range(T):
    a, b= map(int,input().split())
    aa, bb= a, b
    # 결과적으로 b에 최대공약수가 들어감
    while a%b!=0:
        a,b = b, a%b
    print(aa*bb//b)
    
