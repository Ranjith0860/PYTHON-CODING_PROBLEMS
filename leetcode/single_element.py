class Solution:
    def singleNumber(self, nums):
        feq = {}
        for num in nums:
            feq[num] = feq.get(num, 0) + 1
        for num in feq:
            if feq[num] == 1:
                print(num)

# Create object
sol = Solution()

# Call method with argument
sol.singleNumber([1, 2, 3, 2, 1, 1, 2])
