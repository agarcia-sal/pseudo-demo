class Solution:
    def minimumArrayLength(self, nums):
        omega = float('inf')
        i = 0
        while i < len(nums):
            if not (nums[i] >= omega):
                omega = nums[i]
            i += 1

        beta = 0
        j = 0
        while j < len(nums):
            if not (nums[j] != omega):
                beta += 1
            j += 1

        if not (beta != 1):
            return 1
        else:
            return (beta + 1) / 2