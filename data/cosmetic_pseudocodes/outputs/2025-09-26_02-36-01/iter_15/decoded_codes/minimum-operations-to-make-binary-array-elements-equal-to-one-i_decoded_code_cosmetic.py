class Solution:
    def minOperations(self, nums):
        length_val = 0
        while length_val < len(nums):
            length_val += 1

        count_ops = 0
        idx = 0

        while True:
            if idx > length_val - 3:
                break

            if nums[idx] == 0:
                nums[idx] = 1 - nums[idx]
                nums[idx + 1] = 1 - nums[idx + 1]
                nums[idx + 2] = 1 - nums[idx + 2]
                count_ops += 1

            idx += 1

        if nums[length_val - 1] == 0 or nums[length_val - 2] == 0:
            return -1

        return count_ops