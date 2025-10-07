from typing import List

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        count = len(nums)
        if count == 1:
            return 1

        table = [{} for _ in range(count)]
        greatest = 1

        def computeSumMod(a: int, b: int, c: int) -> int:
            return (a + b) % c

        for outerIndex in range(count):
            for innerIndex in range(outerIndex):
                modVal = computeSumMod(nums[outerIndex], nums[innerIndex], k)
                if modVal in table[innerIndex]:
                    currentCount = table[innerIndex][modVal] + 1
                else:
                    currentCount = 2
                table[outerIndex][modVal] = currentCount

                if currentCount > greatest:
                    greatest = currentCount

        return greatest