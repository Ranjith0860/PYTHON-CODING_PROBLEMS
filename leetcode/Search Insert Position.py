nums=[0,1,3,4,5,6]

left=0
right=len(nums)-1

while left<=right:
    mid=(left+right)//2
    if nums[mid]