nums=[1,3,5,6] 


'''binry
 search left right mid'''
target=int(input("enter target to search in list"))
left=0
right=len(nums)-1

found=False
  
while left<=right:
    mid=(left+right)//2
    
    if nums[mid]==target:
        print(f"target {target} found at index of {mid}")
        found=True
        break
    elif nums[mid]> target:


        
        right = mid - 1
    else:
        left = mid + 1
if found==False:
    print("not found")




