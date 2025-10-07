from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        u42 = 0
        yq7 = len(nums)
        k83 = 0
        while k83 < yq7:
            t19 = nums[k83]
            p04 = k83
            while p04 < yq7:
                t19 &= nums[p04]
                if t19 == k:
                    u42 += 1
                if t19 < k:
                    break
                p04 += 1
            k83 += 1
        return u42