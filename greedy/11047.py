n, k = map(int,input().split())
coins = []
for i in range(n):
    coins.append(int(input()))

cnt= 0
for i in range(n-1,-1,-1):
    if k>=coins[i]:
        tmp = k//coins[i]
        k-=(tmp*coins[i])
        cnt+=tmp
    if k==0:
        break
print(cnt)
    
    
