nums = [1, 4, 2, 5, 6, 11, 10, 22, 16]
nums.sort()  # Binary search needs sorted list

target = 3
si = 0
ei = len(nums) - 1
found = False

# You can run the loop for at most log₂(n) times; using a safe limit
for i in range(len(nums)):
    if si > ei:
        break  # Search range is invalid, stop loop

    mid = (si + ei) // 2
    if nums[mid] == target:
        print(f"Target {target} found at index {mid}")
        found = True
        break
    elif nums[mid] < target:
        si = mid + 1
    else:
        ei = mid - 1

if not found:
    print(f"Target {target} not found")
