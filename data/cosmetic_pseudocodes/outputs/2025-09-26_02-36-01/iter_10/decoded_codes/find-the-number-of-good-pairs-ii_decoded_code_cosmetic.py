from collections import Counter
from typing import List

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], k: int) -> int:
        def tallyElements(arr: List[int]) -> Counter:
            frequencyMap = Counter()
            idx = 0
            while idx < len(arr):
                frequencyMap[arr[idx]] += 1
                idx += 1
            return frequencyMap

        duplicatedMapping = tallyElements(nums2)
        accumulatedPairs = 0
        pos = 0

        while True:
            if pos >= len(nums1):
                break
            currentVal = nums1[pos]
            entries = list(duplicatedMapping.items())
            entryIndex = 0

            while entryIndex < len(entries):
                keyElem, valCount = entries[entryIndex]
                if (currentVal % (keyElem * k)) == 0:
                    accumulatedPairs += valCount
                entryIndex += 1
            pos += 1

        return accumulatedPairs