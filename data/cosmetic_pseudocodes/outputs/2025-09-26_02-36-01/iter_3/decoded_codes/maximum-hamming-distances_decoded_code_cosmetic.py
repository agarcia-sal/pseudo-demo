from typing import List

class Solution:
    def maxHammingDistances(self, nums: List[int], m: int) -> List[int]:
        binReprs = []
        for num in nums:
            paddedBinary = ''.join(str((num >> bitPos) & 1) for bitPos in range(m - 1, -1, -1))
            binReprs.append(paddedBinary)

        def hamming_distance(bin1: str, bin2: str) -> int:
            distCounter = 0
            for c1, c2 in zip(bin1, bin2):
                if c1 != c2:
                    distCounter += 1
            return distCounter

        results = []
        for i in range(len(nums)):
            maxDistFound = 0
            for j in range(len(nums)):
                if i != j:
                    computedDist = hamming_distance(binReprs[i], binReprs[j])
                    if computedDist > maxDistFound:
                        maxDistFound = computedDist
            results.append(maxDistFound)

        return results