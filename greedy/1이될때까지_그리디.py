# 가능한 최대한 나누기 작업을 수행
# 중요한 것은 K가 2이상이어야 함
# 그럼 항상 나누는 것이 1을 빼는 것보다 빠르게 N을 줄일 수 있다
# 또한 N은 항상 1에 도달할 수 있음 (최적의 해 성립)
import time

start = time.time()
N=25
k=3
count=0
while N!=1:
    if N%k==0:
        N=N//k
        count+=1
    else:
        N-=1
        count+=1
print(count)
end = time.time()
print(end-start)


n, k = map(int, input().split())
start = time.time()
result = 0
while True:
    target = (n//k)*k
    result += (n-target)
    n = target

    if n<k:
        break
    result+=1
    n//=k
result+= (n-1)
print(result)
end = time.time()
print(end-start)
