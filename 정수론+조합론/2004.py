n, m = map(int,input().split())

def two(n):
    res=0
    while n!=0:
        n=n//2
        res+=n
    return res
def five(n):
    res=0
    while n!=0:
        n=n//5
        res+=n
    return res

print(min(two(n)-two(m)-two(n-m), five(n)-five(m)-five(n-m)))
