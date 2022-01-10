# 병사 배치하기
"""
N명의 병사가 무작위로 나열
전투력이 높은 병사가 앞쪽에 오도록 내림차순으로 배치하고자 한다.
배치 과정에서는 특정한 위치에 있는 병사를 열외시키고
남아있는 병사의 수가 최대가 되록 하고 싶다.

# 이 문제의 기본 아이디어는 가장 긴 증가하는 부분 수열 (LIS)
# 본 문제는 가장 긴 감소하는 부분 수열을 찾는 문제로 치
"""

# 15 11 4 8 5 2 4

N = int(input())
arr = list(map(int,input().split()))

res = [1]*N

for i in range(1, N):
    for j in range(i):
        res[i] = max(res[i],res[j]+1) if arr[j] > arr[i] else res[i]
print(N-res[N-1])
