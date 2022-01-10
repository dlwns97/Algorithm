# Fibonacci topdown, bottomup

#1 topdown

fib = [0]*100

def fibo(x):
    if x==1 or x==2:
        return 1
    if fib[x]!=0:
        return fib[x]
    fib[x] = fibo(x-1) + fibo(x-2)
    return fib[x]

print(fibo(99))

#2. botomdown

d = [0]*100
d[1] = 1
d[2] = 1
n=99

for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]
print(d[99])



