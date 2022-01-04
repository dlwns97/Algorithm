# 모험가 길드
# 공포도가 X인 모험가는 반드시 X명이상으로 구성한 모험가 그룹

N = map(int, input())
arr = list(map(int, input().split()))

arr = sorted(arr, reverse=True)
res = 0
key = arr[0]
count=0
for item in arr:
    count+=1
    if item>key:
        key = item
    if count==key:
        count=0
        key=0
        res+=1
print(res)
    

# 오름차순 정렬 이후 공포도가 낮은 모험가부터 하나씩 확인
# 현재 그룹에 포함된 모험가의 수가 현재 확인하고 있는 공포도보다
# 크거나 같자면 이를 그룹으로 설정하면 된다.
# 이러한 방법을 이용하면 공포도가 오름차순으로 정렬되어 있다는 점에서
# 항상 최소한의 모험가의 수만 포함하여 그룹을 결성하게 된다.

n=int(input())
data = list(map(int, input().split()))
data.sort()

result = 0 # 총 그룹의 수
count = 0 # 현재 그룹에 포함된 모험가의 수

for i in data: # 공포도를 낮은 것부터 하나씩 확인하며
    count+=1 # 현재 그룹에 해당 모험가를 포함시키기
    if count>=i : # 현재 그룹에 포함된 모험가의 수가 현재의 공포도 이상이라면, 그룹 결성
        result += 1 # 총 그룹의 수 증가
        count = 0 # 현재 그룹에 포함된 모험가의 수 초기화
print(result)
