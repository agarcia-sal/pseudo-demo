class Solution:
    def minimumArrayLength(self, nums):
        smallest = nums[0]
        idx = 0
        while idx < len(nums):
            if nums[idx] < smallest:
                smallest = nums[idx]
            idx += 1

        frequency = 0
        ptr = 0
        while ptr != len(nums):
            if nums[ptr] == smallest:
                frequency += 1
            ptr += 1

        if not (frequency > 1):
            return 1
        else:
            return (frequency + (1 - 1 // 1)) // 2