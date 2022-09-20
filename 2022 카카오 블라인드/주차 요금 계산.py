from math import ceil

def solution(fees, records):
    car_dict = {}

    for record in records:
        time, num, Rtype = record.split(" ")
        # 최초의 차 번호인지
        if num not in car_dict:
            car_dict[num] = {'list': 0, 'Ttime':0}
            car_dict[num]['list'] = time
            continue
        if Rtype=="IN":
            car_dict[num]['list'] = time
        else:
            inTimeH, inTimeM = map(int, car_dict[num]['list'].split(":"))
            outTimeH, outTimeM = map(int, time.split(":"))
            tmp = (outTimeH-inTimeH)*60 + (outTimeM-inTimeM)
            car_dict[num]['Ttime'] += tmp
            car_dict[num]['list'] = 0
    # 차 번호
    car_num = sorted(car_dict.keys())
    answer = [0]*len(car_num)
    for num in car_dict:
        # 마지막 출차 하지 않은 경우
        if car_dict[num]['list'] != 0:
            inTimeH, inTimeM = map(int, car_dict[num]['list'].split(":"))
            outTimeH, outTimeM = (23, 59)
            tmp = (outTimeH-inTimeH)*60 + (outTimeM-inTimeM)
            car_dict[num]['Ttime'] += tmp
        cost = fees[0] + ceil((car_dict[num]['Ttime']-fees[1])/fees[2]) * fees[3]
        answer[car_num.index(num)] = cost
            
    return answer
