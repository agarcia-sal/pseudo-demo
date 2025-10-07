from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        v0 = 0
        v1 = len(nums)
        v2 = 0
        while v2 < v1:
            v3 = v2
            v4 = nums[v2]
            while True:
                v4 = v4 & nums[v3]
                if v4 == k:
                    v0 += 1
                if not (v4 >= k):
                    break
                v3 += 1
                if v3 == v1:
                    break
            v2 += 1
        return v0