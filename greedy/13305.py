N=int(input())
dist = list(map(int,input().split()))
price = list(map(int,input().split()))

i, j, ans = (0,0,0)

while j<len(dist):
    cnt=0
    for x in range(i+1, len(price)):
        ans+=price[i]*dist[j]
        j+=1
        cnt+=1
        if price[i]>price[x]:
            break
    i+=cnt
print(ans)
