import math

T=int(input())

s=[]
gcd = 0
for i in range(T):
    s.append(int(input()))
    if i==1:
        gcd = abs(s[1]-s[0])
    gcd = math.gcd(abs(s[i]-s[i-1]), gcd)
a=[]
for i in range(2, int(gcd**0.5)+1):
    if gcd%i==0:
        a.append(i)
        a.append(gcd//i)
a.append(gcd)
a=list(set(a))
a.sort()
for item in a:
    print(item, end=' ')
print()
