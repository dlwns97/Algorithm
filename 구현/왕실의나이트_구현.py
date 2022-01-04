# 왕실의 나이트
"""
8*8 좌표 평면, L자 형태로만 이동할 수 있음

현 위치에서 나이트가 이동할 수 있는 경우의 수를 출력
"""

s = input()
x = ord(s[0])-ord('a')+1
y = int(s[1])

dx = [-2, -2, 2, 2, -1, -1, 1, 1]
dy = [-1, 1, -1, 1, -2, 2, -2, 2]

count = 0

for i in range(len(dx)):
    nx = x + dx[i]
    ny = y + dy[i]

    if nx<1 or ny< 1 or nx > 8 or ny> 8:
        continue
    count+=1
print(count)
