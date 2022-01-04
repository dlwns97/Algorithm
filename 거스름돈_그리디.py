# 거스름 돈

N= int(input())

res = 0

arr = [500, 100, 50, 10]

for coin in arr:
    res+=N//coin
    N%=coin

if N==0:
    print(res)
else:
    print('fail')
