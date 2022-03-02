n=int(input())
s=[]
for i in range(n):
    s.append(int(input()))
idx=0
num=[]
stack=[]
flag=0
for item in s:
    if idx<item:
        while idx!=item:
            idx+=1
            num.append(idx)
            stack.append('+')
    if idx==item:
        stack.append('-')
        num.pop()
    if idx>item:
        tmp=num[-1]
        if tmp==item:
            stack.append('-')
            num.pop()
        else:
            print("NO")
            flag=1
            break
if flag==0:
    for item in stack:
        print(item)

