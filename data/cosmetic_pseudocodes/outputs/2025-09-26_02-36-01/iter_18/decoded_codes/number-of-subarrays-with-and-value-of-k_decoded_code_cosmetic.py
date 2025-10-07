from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        delta = 0
        dim = len(nums)
        idx_outer = 0

        while idx_outer < dim:
            val_mask = nums[idx_outer]
            idx_inner = idx_outer

            while True:
                val_mask &= nums[idx_inner]
                if val_mask == k:
                    delta += 1
                if val_mask < k:
                    break
                idx_inner += 1
                if idx_inner == dim:
                    break

            idx_outer += 1

        return delta