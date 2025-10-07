from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        lengthOfNums = len(nums)
        limitPrimary = lengthOfNums
        accumulatorCount = 0
        indexPrimary = 0

        while indexPrimary <= limitPrimary - 1:
            tempAnd = nums[indexPrimary]
            indexSecondary = indexPrimary
            while True:
                tempAnd &= nums[indexSecondary]
                if tempAnd == k:
                    accumulatorCount += 1
                if tempAnd < k:
                    break
                indexSecondary += 1
                if indexSecondary > limitPrimary - 1:
                    break
            indexPrimary += 1

        return accumulatorCount