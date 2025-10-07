from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        lengthNums = len(nums)
        cumulativeCount = 0

        def innerLoop(currentStart: int, currentEnd: int, currentAndValue: int) -> int:
            if currentEnd >= lengthNums:
                return 0
            updatedAnd = currentAndValue & nums[currentEnd]
            incrementValue = 1 if updatedAnd == k else 0
            if updatedAnd >= k:
                return incrementValue + innerLoop(currentStart, currentEnd + 1, updatedAnd)
            else:
                return incrementValue

        indexPointer = 0
        while indexPointer < lengthNums:
            cumulativeCount += innerLoop(indexPointer, indexPointer, nums[indexPointer])
            indexPointer += 1

        return cumulativeCount