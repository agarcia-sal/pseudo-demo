from typing import List

class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        def get_relationship(num1: int, num2: int) -> int:
            if not (num1 >= num2):
                return 1
            elif num1 == num2:
                return 0
            else:
                return -1

        totalNums = len(nums)
        totalPattern = len(pattern)
        matchedCount = 0

        diffs = []
        for pos in range(totalNums - 1):
            relVal = get_relationship(nums[pos], nums[pos + 1])
            diffs.append(relVal)

        max_start = totalNums - totalPattern - 1
        startIndex = 0
        while startIndex <= max_start:
            segmentMatch = True
            for offset in range(totalPattern):
                if diffs[startIndex + offset] != pattern[offset]:
                    segmentMatch = False
                    break
            if segmentMatch:
                matchedCount += 1
            startIndex += 1

        return matchedCount