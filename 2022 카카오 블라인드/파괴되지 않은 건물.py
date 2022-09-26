def solution(board, skill):
    answer = 0
    skills = [[0] * (len(board[0]) + 1) for _ in range(len(board) + 1)]
    
    for item in skill:
        sType, r1, c1, r2, c2, degree = item
        # 누적 합을 이용하여 시간 초과 탈피
        skills[r1][c1] += degree*(-1) if sType==1 else degree
        skills[r1][c2+1] += degree if sType==1 else degree*(-1)
        skills[r2+1][c1] += degree if sType==1 else degree*(-1)
        skills[r2+1][c2+1] += degree*(-1) if sType==1 else degree
    # 행, 열 방향 누적 합 - 순서 무관
    for i in range(len(skills)-1):
        for j in range(len(skills[0])-1):
            skills[i][j+1] += skills[i][j]
    for j in range(len(skills[0])-1):
        for i in range(len(skills)-1):
            skills[i+1][j] += skills[i][j]
    # board에 반영
    for i in range(len(board)):
        for j in range(len(board[0])):
            board[i][j]+=skills[i][j]
        answer+=len([a for a in board[i] if a>0])
    
    return answer
