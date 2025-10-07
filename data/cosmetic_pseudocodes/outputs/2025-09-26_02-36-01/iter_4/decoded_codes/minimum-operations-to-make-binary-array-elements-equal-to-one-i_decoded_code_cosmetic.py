from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        length = len(nums)
        countOps = 0
        index = 0
        while index < length - 2:
            if nums[index] == 0:
                nums[index] = 1 - nums[index]
                nums[index + 1] = 1 - nums[index + 1]
                nums[index + 2] = 1 - nums[index + 2]
                countOps += 1
            index += 1
        if nums[length - 1] == 0 or nums[length - 2] == 0:
            return -1
        return countOps