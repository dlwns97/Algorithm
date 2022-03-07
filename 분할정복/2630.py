import sys

input = sys.stdin.readline
n= int(input())

square = []
for i in range(n):
    square.append(list(map(int,input().rstrip().split())))

b, w = 0, 0 # blue and white

def check(x,y,n):
    global b, w
    color = square[x][y]
    flag=True

    for i in range(n):
        if not flag:
            break
        for j in range(n):
            if square[x+i][y+j]!=color:
                flag=False
                check(x,y,n//2)
                check(x,y+n//2,n//2)
                check(x+n//2,y,n//2)
                check(x+n//2,y+n//2,n//2)
                break
    if flag:
        if color:
            b+=1
        else:
            w+=1
check(0,0,n)
print(w)
print(b)
