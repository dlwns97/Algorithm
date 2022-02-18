T=int(input())

dp = [(1,0), (0,1)]

for i in range(2, 41):
    item = dp[i-2][0]+dp[i-1][0], dp[i-2][1]+dp[i-1][1]
    dp.append(item)

for i in range(T):
    N=int(input())
    print(dp[N][0], dp[N][1])

    
