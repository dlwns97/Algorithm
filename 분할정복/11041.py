"""
페르마 소정리
a^(p-1)===1(mod p)

ex) (64^70)%71=1

=> a^p%p=a

=> a^(p-2)=a^-1(MOD p)

nCk%p = n!((n-k)!k!)^(p-2)%p
"""

n, k = map(int,input().split())
p = 1000000007

def power(n, k):
    
    if k==0:
        return 1
    elif k==1:
        return n
    
    tmp = power(n, k//2)
    
    if k%2==0:
        return tmp*tmp%p
    else:
        return tmp*tmp*n%p

def fact(n):
    tmp=1
    for i in range(2,n+1):
        tmp = (tmp*i)%p
    return tmp

par = fact(n)
chi = fact(n-k) * fact(k) % p

print(par*power(chi, p-2) % p)
    
