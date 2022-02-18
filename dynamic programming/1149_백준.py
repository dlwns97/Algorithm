N=int(input())

p=[]
for i in range(N):
    p.append(list(map(int,input().split())))
dp = [p[0]]
for i in range(1, N):
    a = p[i][0]+min(dp[i-1][1],dp[i-1][2])
    b = p[i][1]+min(dp[i-1][0],dp[i-1][2])
    c = p[i][2]+min(dp[i-1][0],dp[i-1][1])
    dp.append((a,b,c))
print(min(dp[N-1]))
