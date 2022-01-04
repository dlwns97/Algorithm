# bfs
"""
각 간선의 비용이 모두 동일한 상황에서
최단 거리 문제를 해결하기 위한 목적으로 사용되기도 함 
"""
from collections import deque

# 그래프 정보
graph = [
    [],
    [2,3,8],
    [1,7],
    [1,4,5],
    [3,5],
    [3,4],
    [7],
    [2,6,8],
    [1,7]
]
# 방문 정보
visited = [False]*9

# BFS 메서드 정의

def bfs(graph, start, visited):
    # 큐(queue) 구현을 위해 deque 라이브러리 사용
    queue = deque([start])
    # 현재 노드를 방문 처리
    visited[start] = True
    # 큐가 빌 때까지 반복
    while queue:
        v = queue.popleft()
        print(v, end=' ')
        # 아직 방문하지 않은 인접한 원소들을 큐에 삽입
        for i in graph[v]:
            if not visited[i]:
                visited[i]=True
                queue.append(i)
bfs(graph, 1, visited)
