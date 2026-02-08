def removeElement(nums, value):
    k = 0  # Index to place the next valid element

    for i in range(len(nums)):
        if nums[i] != value:
            nums[k] = nums[i]
            k += 1

    return k
nums = [0, 1, 2, 2, 3, 0, 4, 2]
value = 3

k = removeElement(nums, value)
print(k)        # 5
print(nums[:k]) # [0, 1, 3, 0, 4]

