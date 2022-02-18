T=int(input())
nums=[]
for i in range(T):
    nums.append(int(input()))
max_ = max(nums)

x=[0,1,1,1,2,2,3,4,5,7,9]

if max_<=10:
    for item in nums:
        print(x[item])
else:
    for i in range(11, max_+1):
        x.append(x[i-3]+x[i-2])
    for item in nums:
        print(x[item])
        
    
