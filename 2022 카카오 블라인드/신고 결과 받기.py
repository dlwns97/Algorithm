# 최초 풀이

def solution(id_list, report, k):
    answer = [0]*len(id_list)
    # 몇 번 신고 당했는 지, 정지 대상인지 파악 위해
    report_num = [0]*len(id_list)
    # dictionary로 id_list마다 누구를 신고했는지, id_list 순서대로 받은 메일을 저장하는 list
    report_list = { id : [] for id in id_list }
    
    # report 내용 읽기
    for re in report:
        user1, user2 = re.split(" ")
        if user2 not in report_list[user1]:
            report_list[user1].append(user2)
            idx = id_list.index(user2)
            report_num[idx]+=1
    # 정지 인원 파악하기
    for idx, num in enumerate(report_num):
        if num>=k:
            id = id_list[idx]
            for i in range(len(id_list)):
                if id in report_list[id_list[i]]:
                    answer[i]+=1
                
    
    return answer

# 모범 풀이

def solution(id_list, report, k):
    answer = [0]*len(id_list)
    report_list = {id:0 for id in id_list}

    # 신고 당한 횟수 파악
    for re in set(report):
        report_list[re.split(" ")[1]]+=1

    # 보낼 메일 횟수 파악
    for re in set(report):
        if report_list[re.split(" ")[1]]>=k:
            answer[id_list.index(re.split(" ")[0])]+=1
    return answer


'''
문제 조건에 동일한 신고자가 동일한 대상을 신고할 수 있지만
신고 횟수가 계산되지 않는다고 했는데

이것을 set으로 활용하여 연산량을 줄일 수 있음
'''
