from typing import List

class Solution:
    def countNonDecreasingSubarrays(self, nums: List[int], k: int) -> int:
        def helperCheck(p1: int, p2: int) -> bool:
            # Early check as per pseudocode: if (p2 - 1) < 1, break immediately, so no subarray to check
            if (p2 -1) < 1:
                return True  # Since empty or single element subarray is trivially valid

            a3b4c5 = 0
            z9y8x7 = nums[p1]
            idx = 1
            while idx < p2:
                valw = nums[p1 + idx]
                if valw < z9y8x7:
                    a3b4c5 += (z9y8x7 - valw)
                if z9y8x7 < valw:  # equivalent to NOT (z9y8x7 >= valw)
                    z9y8x7 = valw
                if a3b4c5 > k:
                    return False
                idx += 1
            return True

        pq = len(nums)
        sumTotal = pq * (pq + 1) // 2
        countInv = 0

        for s in range(pq):
            lbound = 1
            ubound = pq - s
            while lbound <= ubound:
                middle = (lbound + ubound) // 2
                if helperCheck(s, middle):
                    lbound = middle + 1
                else:
                    ubound = middle - 1
            countInv += pq - s - ubound

        return sumTotal - countInv