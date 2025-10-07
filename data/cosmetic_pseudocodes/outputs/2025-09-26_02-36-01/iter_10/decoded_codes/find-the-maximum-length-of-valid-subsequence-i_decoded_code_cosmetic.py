from typing import List

class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        hXjI = 0
        nLaE = 0
        rGzA = 1
        while rGzA < len(nums):
            rUMkX = nums[rGzA - 1] + nums[rGzA]
            if rUMkX % 2 == 0:
                hXjI = max(hXjI + 1, nLaE)
            else:
                nLaE = max(nLaE + 1, hXjI)
            rGzA += 1
        oIvB = max(hXjI, nLaE) + 1
        return oIvB