def is_prime(n):
    if n<2:
        return 0
    else:
        for i in range(2, int(n**0.5)+1):
            if n%i==0:
                return 0
    return 1

def converter(n, q):
    rev_base = ''
    while n>0:
        n, mod = divmod(n, q)
        rev_base += str(mod)
    return rev_base[::-1]

def solution(n, k):
    new_n = converter(n, k)
    answer = 0
    # 0을 포함하지 않는 소수 => 0으로 split?
    num_list = new_n.split('0')
    for num in num_list:
        if num!="":
            answer+=is_prime(int(num))
    return answer
