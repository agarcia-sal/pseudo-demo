from typing import List

class Solution:
    def maxHammingDistances(self, nums: List[int], m: int) -> List[int]:
        def hamming_distance(bin1: str, bin2: str) -> int:
            # Count differing bits between two binary strings
            acc_dist = 0
            for b1, b2 in zip(bin1, bin2):
                if b1 != b2:
                    acc_dist += 1
            return acc_dist

        uver = []
        for tvi in nums:
            tempbin = []
            for tmp_idx in range(m):
                bitmask = 1 << (m - 1 - tmp_idx)
                tempbin.append('1' if (tvi & bitmask) != 0 else '0')
            uver.append(''.join(tempbin))

        resarr = []
        n = len(nums)
        for ix in range(n):
            maxval = 0
            for jx in range(n):
                if ix != jx:
                    tmpdist = hamming_distance(uver[ix], uver[jx])
                    if tmpdist > maxval:
                        maxval = tmpdist
            resarr.append(maxval)

        return resarr