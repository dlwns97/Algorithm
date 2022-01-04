# dfs

def dfs(graph, v, visited):
    # 현재 노드를 방문 처리
    visited[v]=True
    print(v, end=' ')
    # 현재 노드와 연결된 다른 노드를 재귀적으로 방문
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)
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

dfs(graph,1,visited)

"""
그래프와 방문 정보를 보면 index 0을 이용하지 않는다.
실제 그래프에서 노드 번호가 1부터 시작했기 때문에 그렇게 진행했다.
"""
