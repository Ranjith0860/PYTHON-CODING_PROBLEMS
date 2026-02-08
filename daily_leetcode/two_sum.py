# noramal apporach



def TwoSum(nums,target):
    for i in range(len(nums)):
        for j in range(i+1,len(nums)):
            if nums[i]+nums[j]==target:
                print(f"Target found at index {i} {j} so \n index value  {nums[i]} + {nums[j]} = {target}")
                return   # we use return after print beacuse it stops executes below code after if exsists
            
    print("target not found")
nums=[2,7,9,8]
target=9
TwoSum(nums,target) 


# Best approach       #    

def TwoSumBestApp(nums1,target):
    nums1.sort()
    left,right=0,len(nums1)-1
    while  left<right:
        sum=nums1[left]+nums1[right] 
        if sum== target:
            print(left,right)
            return
        elif sum<target: 
            left+=1
        else:
            right+=1
    print('not found')
    
nums1=[1,2,4]
target=9
TwoSumBestApp(nums1,target)


