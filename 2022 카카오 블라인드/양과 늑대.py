from collections import defaultdict
from copy import deepcopy

tree = defaultdict(list)
is_wolf = list()
max_sheep = 0

def dfs(node, queue, nSheep, nWolf, visited):
    global max_sheep
    
    # 이미 방문한 노드
    if visited[node]==True: 
        return
    visited[node]=True
    
    # 양이거나 늑대
    if is_wolf[node]==1:
        nWolf+=1
    else:
        nSheep+=1
    # 늑대가 양보다 많은 경우(실패 조건)
    if nWolf>=nSheep:
        return
    # 최대 양의 수 최신화
    max_sheep = max(max_sheep, nSheep)
    
    # 다음 노드 탐색
    # 다음 노드를 탐색할 때, 이미 탐색한 노드는 queue에 없어도 됨
    # deepcopy를 안쓰면 visited list가 계속 변하기 때문에
    # 한 가지의 탐색이 다른 가지에 주지말아야 할 영향을 주지 않기 위해
    queue.extend(tree[node])
    for newNode in queue:
        dfs(newNode, [nod for nod in queue if nod != newNode and not visited[nod]],
           nSheep, nWolf, deepcopy(visited))

def solution(info, edges):
    # global을 쓰는 이유는 재귀에서 계속 영향을 받도록
    # 어느 순간이 최대 순간인지 알 수 없으므로
    global tree, is_wolf, max_sheep
    is_wolf = info
    visited = [False]*len(info)
    
    for from_, to_ in edges:
        tree[from_].append(to_)
    
    dfs(0, [], 0, 0, visited)
    return max_sheep
