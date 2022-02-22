N=int(input())
time = []
ans = []
for i in range(N):
    a, b = map(int,input().split())
    time.append([a,b])

time.sort(key=lambda x:(x[1],x[0]))

ans.append(time[0])
for i in range(1,N):
    if time[i][0]>=ans[-1][1]:
        ans.append(time[i])
print(len(ans))
