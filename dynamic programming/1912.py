"""
나를 포함한 합이

앞에거까지 + 나 , 나 중에 큰 값을 선택
"""

N=int(input())
s=list(map(int,input().split()))

dp=[0]*N
dp[0]=s[0]

for i in range(1, N):
    dp[i]=max(dp[i-1]+s[i],s[i])
print(max(dp))
