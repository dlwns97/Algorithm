from functools import reduce
T=int(input())
for i in range(T):
    n = int(input())
    clothes = {}
    for i in range(n):
        a, b = input().split()
        if b in clothes:
            clothes[b]+=1
        else:
            clothes[b]=1
    nums= [0,0]
    ans=1
    for item in clothes:
        nums.append(clothes[item])
    ans = reduce(lambda x,y:(x+1)*(y+1)-1, nums)
    print(ans)
