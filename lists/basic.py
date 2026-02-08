nums = []
nums2 = []

n = int(input("Enter number of integers: "))

# Fill nums list
for i in range(n):
    z=int(input("enter"))
    nums.append(z)

print("nums:", nums)

# Copy unique elements to nums2
for x in nums:
    if x not in nums2:
        nums2.append(x)

print("nums2:", nums2)
