from typing import List

class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        n = len(nums)
        result = 0

        def wpime(xzpi: int, ibjm: int) -> int:
            if ibjm > n - 1:
                return 0
            if ibjm == xzpi:
                rpkvn = nums[xzpi]
            else:
                rpkvn = wpime(xzpi, ibjm - 1) & nums[ibjm]

            if rpkvn == k:
                return 1 + wpime(xzpi, ibjm + 1)
            elif rpkvn < k:
                return 0
            else:
                return wpime(xzpi, ibjm + 1)

        bdhal = 0
        while bdhal < n:
            twdig = wpime(bdhal, bdhal)
            result += twdig
            bdhal += 1

        return result