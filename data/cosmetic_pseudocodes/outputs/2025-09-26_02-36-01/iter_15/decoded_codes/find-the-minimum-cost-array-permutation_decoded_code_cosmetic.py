from math import inf
from typing import List

class Solution:
    def findPermutation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        full_mask = (1 << n) - 1
        memo = {}

        def dfs(bitmask: int, previous: int) -> int:
            if bitmask == full_mask:
                return abs(nums[previous] - nums[0])
            if (bitmask, previous) in memo:
                return memo[(bitmask, previous)]

            minimalDifference = inf
            for index in range(n):
                if (bitmask >> index) & 1 == 0:
                    nextBitmask = bitmask | (1 << index)
                    difference = abs(nums[previous] - nums[index]) + dfs(nextBitmask, index)
                    if difference < minimalDifference:
                        minimalDifference = difference
            memo[(bitmask, previous)] = minimalDifference
            return minimalDifference

        ans = []
        def g(currentMask: int, lastIndex: int):
            ans.append(lastIndex)
            if currentMask == full_mask:
                return
            optimal = dfs(currentMask, lastIndex)
            position = 0
            while True:
                if position >= n:
                    break
                if ((currentMask >> position) & 1) == 0:
                    newMask = currentMask | (1 << position)
                    candidate = abs(nums[lastIndex] - nums[position]) + dfs(newMask, position)
                    if candidate == optimal:
                        g(newMask, position)
                        break
                position += 1

        g(1, 0)
        return ans