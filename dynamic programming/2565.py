"""
연결된 오른쪽 전봇대를 순서대로 나열하면

8 2 9 1 4 6 7 10

전깃줄이 교차하지 않으려면 한 방향으로 나열되어야 함

증가하는 방향이나 감소하는 방향
"""
N = int(input())
a = []
for i in range(N):
    x, y = map(int,input().split())
    a.append([x,y])
a.sort(key=lambda x:x[0])
s = [x[1] for x in a]

dp_u = [0]*N

for i in range(N):
    for j in range(i):
        if s[j]<s[i] and dp_u[i]<dp_u[j]:
            dp_u[i] = dp_u[j]
    dp_u[i]+=1
print(N-max(dp_u))
