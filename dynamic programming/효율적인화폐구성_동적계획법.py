# 효율적인 화폐 구성

"""
N가지 종류의 화폐가 있을 때, 화폐의 개수를 최소한으로 이용해서
그 가치의 합이 M원이 되도록
"""

N, M = map(int,input().split())
arr = [0]*N
for i in range(N):
    arr[i] = int(input())
arr.sort()

res = [-1]*10001

for item in arr:
    res[item]=1
for i in range(min(arr)+1, 10001):
    for item in arr:
        if res[i-item]!=-1:
            if res[i]==-1:
                res[i] = res[i-item]+1
            else:
                res[i]=min(res[i],res[i-item]+1)
print(res[M])

N, M = map(int,input().split())
arr = [0]*N
for i in range(N):
    arr[i] = int(input())
arr.sort()

res = [10001]*10001
for item in arr:
    res[item]=1
for i in range(min(arr)+1, 10001):
    for item in arr:
        res[i] = min(res[i],res[i-item]+1)
print(res[M] if res[M]!=10001 else -1)
    
