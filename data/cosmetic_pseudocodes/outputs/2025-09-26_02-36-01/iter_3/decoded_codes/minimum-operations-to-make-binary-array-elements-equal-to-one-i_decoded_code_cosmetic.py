from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        lengthVar = len(nums)
        countOps = 0
        indexVar = 0
        while indexVar <= lengthVar - 3:
            if nums[indexVar] == 0:
                # Flip nums[indexVar], nums[indexVar + 1], nums[indexVar + 2]
                nums[indexVar] = 1 - nums[indexVar]
                nums[indexVar + 1] = 1 - nums[indexVar + 1]
                nums[indexVar + 2] = 1 - nums[indexVar + 2]
                countOps += 1
            indexVar += 1
        if nums[lengthVar - 1] == 0 or nums[lengthVar - 2] == 0:
            return -1
        return countOps