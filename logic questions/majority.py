nums=[1,2,3,2,1,3,2,2,2]

freq={}
for num in nums:
    if num in freq:
          freq[num]+=1
    else:
        freq[num]=1
majority=max(freq,key=freq.get)
print(f"{majority}") 





num,count=nums[0],1

for i in range(1,len(nums)):
     if num==nums[i]:
          count+=1
     else:
          count-=1
          if count<0:
               num=nums[i]

               
               count=1
print(f"{num}")
            