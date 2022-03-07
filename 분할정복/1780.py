import sys
input = sys.stdin.readline

n = int(input())

a,b,c = 0,0,0
paper=[]
for i in range(n):
    paper.append(list(map(int,input().rstrip().split())))

def check(x,y,n):
    global a,b,c
    num=paper[x][y]
    for i in range(n):
        for j in range(n):
            if num!=paper[x+i][y+j]:
                check(x,y,n//3)
                check(x,y+n//3,n//3)
                check(x,y+2*n//3,n//3)
                check(x+n//3,y,n//3)
                check(x+n//3,y+n//3,n//3)
                check(x+n//3,y+2*n//3,n//3)
                check(x+2*n//3,y,n//3)
                check(x+2*n//3,y+n//3,n//3)
                check(x+2*n//3,y+2*n//3,n//3)
                return
    if num==1:
        a+=1
    elif num==0:
        b+=1
    else:
        c+=1

check(0,0,n)
print("%d\n%d\n%d"%(c,b,a))
