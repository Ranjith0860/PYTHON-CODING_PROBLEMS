nums = list(map(int, input("enter numbers that convert to dictonary").split(" ")))
dic={}

for i in nums:
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
print(nums)
print(dic)