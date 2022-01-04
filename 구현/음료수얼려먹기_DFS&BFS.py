# 음료수 얼려 먹기 

"""
1. 특정한 지점의 주변 상, 하, 좌, 우를 살펴본 뒤에 주변 지점 중에서 값이 '0'
이면서 아직 방문하지 않은 지점이 있다면 해당 지점을 방문

2. 방문한 지점에서 다시 상, 하, 좌, 우를 살펴보면서 방문을 진행하는 과정을 반복
하면, 연결된 모든 지점을 방문할 수 있습니다.

3. 모든 노드에 대하여 1~2 번의 과정을 반복하며, 방문하지 않은 지점의 수를 카운트 
"""

def dfs(x,y):
    # 주어진 범위를 벗어나는 경우에 종료
    if x<= -1 or x>=n or y<=-1 or y>=m:
        return False
    # 현재 노드를 아직 방문하지 않았다면

    if graph[x][y]==0:
        graph[x][y]=1
        # 상, 하, 좌, 우의 위치들도 모두 재귀적으로 호출
        dfs(x-1, y)
        dfs(x, y-1)
        dfs(x+1, y)
        dfs(x, y+1)
        return True
    return False

# N,M 입력
n, m = map(int, input().split())

# 2차원 그래프
graph=[]
for i in range(n):
    graph.append(list(map(int, input())))

# 모든 노드에 대하여 음료수 채우기
result = 0
"""
 최초의 루트노드에서만 result+=1이 발생함
 메인 반복문으로의 반환은 루트 노드에서만 일어나기 때문임 
"""
for i in range(n):
    for j in range(m):
        # 현재 위치에서 DFS 수행
        if dfs(i, j) == True:
            result+=1
print(result)
