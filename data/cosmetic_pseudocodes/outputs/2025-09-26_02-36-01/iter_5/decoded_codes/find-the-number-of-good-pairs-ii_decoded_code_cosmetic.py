from collections import defaultdict
from typing import List

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        def helperCount(collection: List[int]) -> dict:
            freqMap = defaultdict(int)
            def tally(index: int) -> None:
                if index >= len(collection):
                    return
                val = collection[index]
                freqMap[val] += 1
                tally(index + 1)
            tally(0)
            return freqMap

        mapping = helperCount(nums2)
        totalPairs = 0
        pos1 = 0

        while pos1 < len(nums1):
            candidate = nums1[pos1]
            keysList = list(mapping.keys())
            idx = 0
            while idx < len(keysList):
                candidate2 = keysList[idx]
                freqCount = mapping[candidate2]
                keyProduct = candidate2 * k
                modulusResult = candidate % keyProduct
                if modulusResult == 0:
                    totalPairs += freqCount
                idx += 1
            pos1 += 1

        output = totalPairs
        return output