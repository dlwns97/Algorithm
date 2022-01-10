# 개미 전사
"""
각 식량창고에는 정해진 수의 식량을 저장, 개미 전사는 식량창고를 선택적으로
약탈하여 식량을 빼앗을 예정
개미 전사는 최소한 한 칸 이상 떨어진 식량 창고를 약탈해야 함.
"""

N = int(input())
arr = list(map(int,input().split()))

res = [0]*N
res[0] = arr[0]
res[1] = max(arr[0],arr[1])

for i in range(2, N):
    res[i] = max(res[i-1],res[i-2]+arr[i])
print(res[N-1])
