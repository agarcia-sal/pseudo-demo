class Solution:
    def minOperations(self, nums):
        n = len(nums)
        operations = 0

        def flip_triplet(i, end):
            nonlocal operations
            if i >= end:
                return
            if nums[i] == 0:
                nums[i] = 1 - nums[i]
                nums[i + 1] = 1 - nums[i + 1]
                nums[i + 2] = 1 - nums[i + 2]
                operations += 1
            flip_triplet(i + 1, end)

        flip_triplet(0, n - 2)
        if not (nums[n - 1] != 0 and nums[n - 2] != 0):
            return -1
        return operations