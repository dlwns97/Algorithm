N, K = map(int,input().split())
N_,K_=1,1

if K>(N//2):
    K=N-K

for i in range(1,K+1):
    N_*=(N-i+1)
    K_*=i
print((N_//K_)%10007)
    


"""
dynamic programming을 이용한 풀이
"""
p = [[0] * 1 for i in range(1001)]
dp[1].append(1)
for i in range(2, 1001):
    for j in range(1, i + 1):
        if j == 1:
            dp[i].append(1)
        elif j == i:
            dp[i].append(1)
        else:
            dp[i].append(dp[i - 1][j - 1] + dp[i - 1][j])
print(dp[n + 1][k + 1] % 10007)
