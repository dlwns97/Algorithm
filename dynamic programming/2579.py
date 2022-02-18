N=int(input())
s=[0]*301
score=[0]*301
for i in range(N):
    s[i]=int(input())
score[0]=s[0]
score[1]=s[0]+s[1]
score[2]=max(s[0]+s[2], s[1]+s[2])

for i in range(3,N):
    score[i] = max(score[i-3]+s[i-1]+s[i],score[i-2]+s[i])

print(score[N-1])
             
