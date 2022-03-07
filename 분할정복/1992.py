import sys
input = sys.stdin.readline

n = int(input())
video=[]
for i in range(n):
    video.append(input().rstrip())

def tree(x,y,n):
    point=video[x][y]
    flag=True

    for i in range(n):
        if flag==False:
            break
        for j in range(n):
            if video[x+i][y+j]!=point:
                flag=False
                print('(',end="")
                tree(x,y,n//2)
                tree(x,y+n//2,n//2)
                tree(x+n//2,y,n//2)
                tree(x+n//2,y+n//2,n//2)
                print(")",end="")
                break
    if flag==True:
        print(point,end="")
tree(0,0,n)
