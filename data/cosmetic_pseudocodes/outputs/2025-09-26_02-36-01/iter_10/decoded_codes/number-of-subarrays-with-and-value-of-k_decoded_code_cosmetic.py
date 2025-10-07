from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        totalLength = len(nums)
        tally = 0

        def bitwiseAND(x: int, y: int) -> int:
            return x & y

        def innerLoop(currIndex: int, endIndex: int, acc: int) -> int:
            nonlocal tally
            if endIndex > totalLength - 1:
                return 0

            acc = bitwiseAND(acc, nums[endIndex])
            if acc == k:
                tally += 1
            if acc < k:
                return 0

            return innerLoop(currIndex, endIndex + 1, acc)

        indexStart = 0
        while indexStart <= totalLength - 1:
            accumulator = nums[indexStart]
            innerLoop(indexStart, indexStart, accumulator)
            indexStart += 1

        return tally