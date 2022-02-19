""" 가장 긴 바이토닉 수열
    앞 뒤로 LIS를 구해서 합하기
"""

N=int(input())
A = list(map(int,input().split()))
B = [0]*N
for i in range(N):
    B[i] = A[i]
B.reverse()
s_f = [0]*N
s_b = [0]*N

for i in range(N):
    for j in range(i):
        if A[j]<A[i] and s_f[i]<s_f[j]:
            s_f[i] = s_f[j]
        if B[j]<B[i] and s_b[i]<s_b[j]:
            s_b[i] = s_b[j]
    s_f[i]+=1
    s_b[i]+=1
for i in range(N):
    s_f[i]+=s_b[N-i-1]-1
print(max(s_f))
