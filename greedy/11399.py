N=int(input())
P=list(map(int,input().split()))
P.sort()
s=0
for i in range(N):
    for j in range(i+1):
        s+=P[j]
print(s)
        
