from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        p = 0
        q = len(nums)
        r = 0

        def flipAt(index: int) -> None:
            nums[index] = 1 - nums[index]

        while p <= q - 3:
            if nums[p] == 0:
                flipAt(p)
                flipAt(p + 1)
                flipAt(p + 2)
                r += 1
            p += 1

        if not (nums[q - 1] != 0 and nums[q - 2] != 0):
            return -1
        return r