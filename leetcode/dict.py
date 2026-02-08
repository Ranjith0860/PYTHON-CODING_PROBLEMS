nums = list(map(int, input("enter numbers that convert to dictonary").split(" ")))

dic={}

for i in nums :
    if i in dic:
        dic[i]+=1
    else:
        dic[i]=1
print(nums)

print(dic)



# Input numbers and keys
nums = list(map(int, input("Enter numbers with space get into dict: ").split()))
nums1 = input("Enter corresponding keys: ").split()

# Check if both lists are of equal length
if len(nums) != len(nums1):
    print("Error: Number of keys and values must match.")
else:
    dic = {}

    # Build dictionary using zip
    for key, value in zip(nums1, nums):
        if key in dic:
            dic[key] += value  # If key repeats, add the value
        else:
            dic[key] = value

    print("Values:", nums)
    print("Keys:", nums1)
    print("Dictionary:", dic)