class Solution:
    def minimumArrayLength(self, nums):
        smallest = nums[0]
        idx = 1
        while idx < len(nums):
            if nums[idx] < smallest:
                smallest = nums[idx]
            idx += 1

        how_many = 0
        i = 0
        while i < len(nums):
            if nums[i] == smallest:
                how_many += 1
            i += 1

        if not (how_many != 1):
            return 1

        result = (how_many + 1) // 2
        return result