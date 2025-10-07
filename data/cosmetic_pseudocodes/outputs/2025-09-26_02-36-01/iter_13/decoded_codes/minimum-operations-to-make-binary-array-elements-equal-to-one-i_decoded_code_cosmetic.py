from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        count = 0
        length = len(nums)
        index = 0

        def invert(x: int) -> int:
            return 1 - x

        while True:
            if index > length - 3:
                break
            if nums[index] == 0:
                nums[index] = invert(nums[index])
                nums[index + 1] = invert(nums[index + 1])
                nums[index + 2] = invert(nums[index + 2])
                count += 1
            index += 1

        if length >= 2 and (nums[length - 1] == 0 or nums[length - 2] == 0):
            return -1

        return count