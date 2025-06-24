nums=[1,3,5,6]


'''binry search left right mid'''
target=5
left=0
right=len(nums)-1

while left<=right:
    mid=(left+right)//2
    if nums[mid]==target:
        print(mid)
        break
    elif nums[mid]> target:
        right = mid - 1
    else:
        left = mid + 1




