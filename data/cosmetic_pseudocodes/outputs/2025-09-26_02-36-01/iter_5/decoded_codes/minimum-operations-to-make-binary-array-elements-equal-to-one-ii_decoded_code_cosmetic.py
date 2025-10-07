class Solution:
    def minOperations(self, nums):
        count_ops = 0
        toggle = 0

        def process(index):
            nonlocal count_ops, toggle
            if index >= len(nums):
                return count_ops

            if (toggle % 2) == 0:
                val_to_check = nums[index]
            else:
                val_to_check = 1 - nums[index]

            if val_to_check == 0:
                count_ops += 1
                toggle += 1

            return process(index + 1)

        return process(0)