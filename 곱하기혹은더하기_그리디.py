# 곱하기 혹은 더하기
import time


s = input()
start = time.time()
result = s[0]
for i in range(len(s)-1):
    tmp1 = result+'+'+s[i+1]
    tmp2 = result+'*'+s[i+1]
    result = tmp1 if eval(tmp1)>=eval(tmp2) else tmp2
print(eval(result))
end = time.time()
print(end-start)

s=input()
start = time.time()
result = int(s[0])
for i in range(1,len(s)):
    num = int(s[i])
    if num<=1 or result<=1:
        result += num
    else:
        result *= num
print(result)
end=time.time()
print(end-start)
