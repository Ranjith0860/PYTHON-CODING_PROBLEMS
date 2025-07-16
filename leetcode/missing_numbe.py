nums=[0,1,3,4,5]

le=len(nums)
for i in range(len(nums)):
    k=i-nums[i]  #le=5+0-0=5,le=5+1-1=5,le=5+2-3=4,le=4+3-4=3,le=3+4-5=2
    le+=k
print(le)



nums = [0, 1, 3, 4, 5]
n = len(nums)  # Since one number is missing, the range is 0 to n

# So we use n (not len(nums)) in the formula because one number is missing
expected_sum = (n * (n + 1)) // 2  # Sum from 0 to n
actual_sum = sum(nums)
missing = expected_sum - actual_sum
print("Missing number:", missing)

