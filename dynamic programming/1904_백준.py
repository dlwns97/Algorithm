N=int(input())

a,b=1,2
ans=0
if N==1:
    print(1)
elif N==2:
    print(2)
else:
    for i in range(3, N+1):
        ans=(a+b)%15746
        a=b
        b=ans
print(ans)
