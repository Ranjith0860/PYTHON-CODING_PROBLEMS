nums=[1,4,5,6,7]

nums.sort()
for i in range(1,len(nums)):
    if nums[i]==nums[i-1]:
        print("true")
        break
else:
    print("false")


s = set()
for i in nums:
    if i in s:
        print("Duplicate found")
        break
    s.add(i)
else:
    print("No duplicates")



hashmap={}
for i in nums:
    if i in hashmap:
        print("dublicate found")
        break
    else:
        hashmap[i]=1
print("false")