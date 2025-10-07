from itertools import combinations
from collections import Counter

class Solution:
    def subsequencesWithMiddleMode(self, nums):
        MODULO_CONST = 1_000_000_007
        lengthNums = len(nums)
        if lengthNums <= 4:
            return 0

        totalMatches = 0
        # Generate all 5-length combinations preserving order
        # Since pseudocode uses GENERATE_COMBINATIONS(nums, 5),
        # interpreted as combinations of indices preserving order
        for currentSeq in combinations(nums, 5):
            frequencyMap = Counter(currentSeq)
            medianVal = currentSeq[2]
            medianCount = frequencyMap[medianVal]

            uniqueModeFlag = True
            for key, countVal in frequencyMap.items():
                if key != medianVal and countVal >= medianCount:
                    uniqueModeFlag = False
                    break

            if uniqueModeFlag:
                totalMatches += 1

        return totalMatches % MODULO_CONST