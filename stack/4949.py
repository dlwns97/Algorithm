import sys

tmp=""
while True:
    tmp = sys.stdin.readline().rstrip()
    if tmp==".":
        break
    stack=[]
    flag=0
    for i in range(len(tmp)):
        if tmp[i]=='(' or tmp[i]=='[':
            stack.append(tmp[i])
        elif tmp[i]==')':
            if len(stack)==0 or stack[-1]=='[':
                flag=1
                break
            else:
                stack.pop()
        elif tmp[i]==']':
            if len(stack)==0 or stack[-1]=='(':
                flag=1
                break
            else:
                stack.pop()
    if len(stack)==0 and flag==0:
        print("yes")
    else:
        print("no")
