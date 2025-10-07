class Solution:
    def canSortArray(self, nums):
        def bitCount(x):
            total = 0
            while x > 0:
                total += x & 1
                x >>= 1
            return total

        length = len(nums)
        target = sorted(nums)

        for _ in range(length):
            for i in range(length - 1):
                if bitCount(nums[i]) == bitCount(nums[i + 1]) and nums[i] > nums[i + 1]:
                    nums[i], nums[i + 1] = nums[i + 1], nums[i]

        return nums == target