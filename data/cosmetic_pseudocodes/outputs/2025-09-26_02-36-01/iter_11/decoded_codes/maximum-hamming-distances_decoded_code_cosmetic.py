from typing import List

class Solution:
    def maxHammingDistances(self, nums: List[int], m: int) -> List[int]:
        omega = []
        alpha = 0
        kappa = len(nums)
        fz0 = m - alpha  # unused variable but preserved as per pseudocode

        def stringify(n: int, length: int) -> str:
            def inner_stringify(x: int, l: int) -> str:
                if l == 0:
                    return ""
                prefix = inner_stringify(x // 2, l - 1)
                bit = x % 2
                return prefix + ("1" if bit == 1 else "0")
            raw_str = inner_stringify(n, length)
            return raw_str

        zq1 = 0
        while zq1 < kappa:
            raw_bin = stringify(nums[zq1], m)
            omega.append(raw_bin)
            zq1 += 1

        retVal = []

        def hamming_distance(bin1: str, bin2: str) -> int:
            distVal = 0
            pos = 0
            length = len(bin1)
            while pos < length:
                if bin1[pos] != bin2[pos]:
                    distVal += 1
                pos += 1
            return distVal

        idxI = 0
        while True:
            if idxI >= kappa:
                break
            maxDTracker = 0

            idxJ = 0
            while idxJ < kappa:
                if idxI != idxJ:
                    tempDist = hamming_distance(omega[idxI], omega[idxJ])
                    if maxDTracker < tempDist:
                        maxDTracker = tempDist
                idxJ += 1

            retVal.append(maxDTracker)
            idxI += 1

        return retVal