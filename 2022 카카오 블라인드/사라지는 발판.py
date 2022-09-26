# 양 플레이어는 최적의 플레이를 합니다.

# 플레이어의 상하좌우를 체크. 이동 가능한 곳으로 이동.

# 현재 board를 graph로 생각?

# 이길 수 있는 플레이어는 최대한 빨리 승리하도록
# 질 수밖에 없는 플레이어는 최대한 오래 버티도록
# 누가 무조건 이기는 플레이어인지 알아야 하나?
# 게임 이론? Tree search를 이용해서 구현
# 각 플레이어가 각자의 최적의 플레이를 하도록

# a, b의 좌표, 이동 거리, board 복사본 유지?

'''
* 종료 조건 *
* 1. 같은 위치에 있는 데 움직일 곳이 없는 경우, 카운트 안함
* 2. 같은 위치에 있는 데 움직일 수 있는 경우, 카운트 함

과정 
# 현재 발판을 지우기
# a면 b를 호출, b면 a를 호출
# 
'''

from copy import deepcopy

answer = 0

def can_move(r, c, board):
    move = []
    for dr, dc in [[0,1],[0,-1],[1,0],[-1,0]]:
        nr=r+dr
        nc=c+dc
        if 0<=nr<len(board) and 0<=nc<len(board[0]) and board[nr][nc]==1:
            move.append((nr,nc))
    return move
def action(board, aloc, bloc, turn):
    # a와 b의 turn에 서로 다른 선택
    
    r, c = aloc if turn%2==0 else bloc
    # 움직일 수 없는 경우
    if len(can_move(r, c, board))==0:
        return (False, 0)
    # 움직이면 끝나는 경우
    if aloc==bloc:
        return (True, 1)
    tmp_board =  deepcopy(board)
    tmp_board[r][c] = 0 # 발판 지우기
    flag = False
    maxTurn, minTurn = 0, float('inf')
    for nr, nc in can_move(r, c, tmp_board):
        if turn%2==0:
            res = action(tmp_board, [nr,nc], bloc, turn+1)
        else:
            res = action(tmp_board, aloc, [nr,nc], turn+1)
        if res[0]==False:
            flag=True
            minTurn = min(minTurn, res[1])
        else:
            maxTurn = max(maxTurn, res[1])
    if flag==True:
        return (flag, minTurn+1)
    else:
        return (flag, maxTurn+1)
    
    
    
def solution(board, aloc, bloc):
    answer = action(board, aloc, bloc, 0)
    return answer

print(solution([[1, 1, 1], [1, 0, 1], [1, 1, 1]],[1, 0],[1, 2]))
