#상하좌우 문제

"""
여행가 A는 N*N 크기의 정사각형 공간 위에 서 있다.
가장 왼쪽 위는 (1, 1)
가장 오른족 아래는 (N, N)
상, 하, 좌, 우로 이동할 수 있다.

정사각형 공간을 벗어나는 움직임은 무시된다.

시뮬레이션 유형으로 분류할 수 있는 구현이 중요한 대표적인 문
"""

N = int(input())
S = input().split()

x=1
y=1

for item in S:
    if item=='R':
        if y==N:
            continue
        else:
            y+=1
    elif item=='L':
        if y==1:
            continue
        else:
            y-=1
    elif item=='U':
        if x==1:
            continue
        else:
            x-=1
    else:
        if x==N:
            continue
        else:
            x+=1
print(x, y)

N = int(input())
S = input().split()

x=1
y=1

dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
move_types = ['L','R','U','D']

for plan in S:
    i = move_types.index(plan)
    nx = x + dx[i]
    ny = y + dy[i]
    if nx<1 or ny<1 or nx>N or ny>N:
        continue
    x,y=nx,ny
print(x, y)
