import math
N=int(input())
nums = list(map(int,input().split()))

for i in range(1, len(nums)):
    if nums[0]%nums[i]==0:
        print("{}/{}".format(nums[0]//nums[i],1))
    else:
        gcd = math.gcd(nums[0],nums[i])
        print("{}/{}".format(nums[0]//gcd,nums[i]//gcd))
    
