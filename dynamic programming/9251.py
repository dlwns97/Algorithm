"""
LCS

C : ACAYKP
A : ACAYKP
...
순차적으로 탐색, 길이를 늘려가면서 체크
"""

s1 = input()
s2 = input()

l1 = len(s1)
dp = [0] * l1

for i in range(len(s2)):
    cnt=0
    for j in range(len(s1)):
        if cnt < dp[j]:
            cnt = dp[j]
        elif s1[j] == s2[i]:
            dp[j] = cnt + 1
print(max(dp))
