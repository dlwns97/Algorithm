n=int(input())
x=list(map(int,input().split()))

dp=[0 for i in range(n)]

for i in range(n):
    for j in range(i):
        if x[i]>x[j] and dp[i]<dp[j]:
            dp[i]=dp[j]
    dp[i]+=1
print(max(dp))
