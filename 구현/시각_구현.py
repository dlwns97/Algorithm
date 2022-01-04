# 시각 문제
"""
00시 00분 00초부터 N시 59분 59초까지 모든 시각 중에서 3이 하나라도 포함되는
모든 경우의 수
"""
import time

N = int(input())

"""
1분에
3 13 23 30~39 43 53 => 15개
3이 들어간 분 일 때 => 60 개

60분 중에 15분은 60개 나머지는 15개

1시간 => 15*60 + 45*15 = 900 + 675 = 1575
시간 중에서 3, 13, 23 => 3600개

"""
start = time.time()
if N<3:
    s = 1575*(N+1)
elif N>=3 and N<13:
    s = 3600 + 1575*N
elif N>=13 and N<23:
    s = 3600*2 + 1575*(N-1)
else:
    s = 3600*3 + 1575*21
end = time.time()
print(s)
print(end-start)


# Brute force
"""
하루는 86400초 밖에 안됨, 전부 다 검사하더라도 충분히 빠름
=> 이러한 근거가 있기 때문에 브루트 포스로 진행할 수 있
"""
h = int(input())
count = 0
start = time.time()
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            if '3' in str(i) + str(j) + str(k):
                count+=1
end = time.time()
print(count)
print(end-start)
