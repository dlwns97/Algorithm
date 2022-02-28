import sys
n = int(sys.stdin.readline().rstrip())

for i in range(n):
    s = sys.stdin.readline().rstrip()
    tmp = ""
    flag=0
    while tmp!=s:
        if flag!=0:
            s=tmp
        tmp=s.replace('()','')
        flag+=1
        
    
    print("NO" if len(s)!=0 else "YES")

#2

a = int(input())
for i in range(a):
    b = input()
    s = list(b)
    sum = 0
    for i in s:
        if i == '(':
            sum += 1
        elif i == ')':
            sum -= 1
        if sum < 0:
            print('NO')
            break
    if sum > 0:
        print('NO')
    elif sum == 0:
        print('YES')
