a, b = map(int,input().split())
if a>b:
    a, b = b, a

for i in range(a, 0, -1):
    if a%i==0 and b%i==0:
        break
g=i
L=(a*b)//g

print(g)
print(L)
