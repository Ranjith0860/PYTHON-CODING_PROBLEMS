nums=[0,1,3,4,5]

le=len(nums)
for i in range(len(nums)):
    le+=i-nums[i]  #5,5,4,-3,
print(le)
