from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        u78 = len(nums)
        j9z = 0
        l1k = 0
        while l1k < u78 - 2:
            g7p = nums[l1k]
            if not (g7p != 0):
                nums[l1k] = 1 - nums[l1k]
                nums[l1k + 1] = 1 - nums[l1k + 1]
                nums[l1k + 2] = 1 - nums[l1k + 2]
                j9z += 1
            l1k += 1
        m3q = nums[u78 - 1]
        v4r = nums[u78 - 2]
        if m3q == 0 or v4r == 0:
            return -1
        return j9z