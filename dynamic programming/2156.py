n=int(input())
s=[0]*10000
score=[0]*10000
for i in range(n):
    s[i]=int(input())

score[0] = s[0]
score[1] = s[0]+s[1]
score[2] = max(score[1], s[0]+s[2], s[1]+s[2])

for i in range(3, n):
    score[i]=max(score[i-3]+s[i-1]+s[i], score[i-2]+s[i], score[i-1])
print(score[n-1])

# 마지막 잔을 꼭 먹을 필요가 없잖아

# 그럼 마지막 잔까지 마셨을 때 최대랑
# 마지막 잔을 마시지 않았을 때의 최대랑 비교
