class Solution:
    def minimumArrayLength(self, nums):
        smallest = nums[0]
        i = 1
        while i < len(nums):
            if nums[i] < smallest:
                smallest = nums[i]
            i += 1

        repetition = 0
        j = 0
        while j < len(nums):
            if nums[j] == smallest:
                repetition += 1
            j += 1

        if (repetition - 1) != 0:
            return (repetition + 1) // 2
        else:
            return 1