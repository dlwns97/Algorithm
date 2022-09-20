# 라이언은 어피치를 가장 큰 점수 차이로 이기기 위해서 n발의 화살을
# 어떤 과녁 점수에 맞혀야 하는지를 구하려고 합니다.

# greedy? dynamic programming? 
# (현재 점수를 먹는 경우, 안 먹는 경우)
# 계속 데이터를 유지할 수 있는 크기가 아님.
# BFS를 통해서 덱에 임시로 데이터를 넣었다가 빼면서 처리해야 할 것 같음
# 이렇게 해야 중간에 처리되는 경우는 따로 처리 됨

# 종료 조건을 찾아야 함

# 1. 화살을 다 쓴 경우
# 2. 0점 과녁에 도달한 경우
# 3. 화살을 더 쏴도 못 이기는 경우

from collections import deque

def bfs(n, info):
    answer = []
    # 현재 쏠 과녁, 화살의 현황
    q = deque([(0,[0,0,0,0,0,0,0,0,0,0,0])])
    
    maxDif = 0
    # BFS
    # 매 과녁마다 새로운 선택지 추가
    while q:
        target, arrow = q.popleft()
        
        # 화살을 다 쏜 경우
        if sum(arrow) == n:
            apeach_s, lion_s = 0, 0
            for i in range(11):
                if info[i]!=0 or arrow[i]!=0:
                    if info[i]>=arrow[i]:
                        apeach_s+=10-i
                    else:
                        lion_s+=10-i
            if apeach_s < lion_s:
                tmp = lion_s-apeach_s
                if maxDif>tmp:
                    continue
                if maxDif<tmp:
                    maxDif=tmp
                    answer.clear()
                answer.append(arrow)
        # 화살을 더 쏜 경우는 실패 조건
        # 화살을 더 쏜 경우는 무조건 실패인데 0점에 도달해 있을 수도 있음
        elif sum(arrow)>n:
            continue
        # 0점 과녁에 도달한 경우
        elif target==10:
            # 화살을 전부 소모해서 첫번째 종료 조건으로
            tmp = arrow.copy()
            tmp[target] = n - sum(tmp)
            q.append((-1, tmp))
        else:
            # 과녁에 쏘는 경우 (어피치를 이겨야 함)
            tmp = arrow.copy()
            tmp[target] = info[target]+1
            q.append((target+1, tmp))
            # 과녁을 포기하는 경우 (0발을 쏨)
            tmp_ = arrow.copy()
            tmp_[target] = 0
            q.append((target+1, tmp_))
    return answer

def solution(n, info):
    candidate = bfs(n, info)
    
    # 후보가 1개
    if len(candidate)==1:
        return candidate[0]
    # 후보가 여러 개
    elif len(candidate)>1:
        return candidate[-1]
    else:
        return [-1]
