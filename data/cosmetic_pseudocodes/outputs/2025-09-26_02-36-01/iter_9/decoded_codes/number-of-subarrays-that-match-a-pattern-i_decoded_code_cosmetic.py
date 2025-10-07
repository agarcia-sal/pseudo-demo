from typing import List

class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:

        def areElementsMatching(indexA: int, indexB: int, sequenceA: List[int], sequenceB: List[int], patternSequence: List[int]) -> bool:
            # Helper to check the relation condition based on patternSequence item
            def checkCondition(itemIndex: int) -> bool:
                if patternSequence[itemIndex] == 1:
                    return sequenceB[indexB + itemIndex + 1] > sequenceB[indexB + itemIndex]
                elif patternSequence[itemIndex] == 0:
                    return sequenceB[indexB + itemIndex + 1] == sequenceB[indexB + itemIndex]
                elif patternSequence[itemIndex] == -1:
                    return sequenceB[indexB + itemIndex + 1] < sequenceB[indexB + itemIndex]
                else:
                    return False

            flagMatch = True
            offset = 0
            while offset < len(patternSequence) - 1 and flagMatch:
                if not checkCondition(offset):
                    flagMatch = False
                offset += 1
            return flagMatch

        lengthNums = len(nums)
        lengthPattern = len(pattern)
        totalMatches = 0
        position = 0
        # The original pseudocode uses `position <= lengthNums - lengthPattern - 1`
        # but if we want a valid subarray of length equal to lengthPattern starting at position,
        # the last start index should be lengthNums - lengthPattern
        # so we preserve original condition but also allow derivatives:
        while position <= lengthNums - lengthPattern - 1:
            if areElementsMatching(position, position, nums, nums, pattern):
                totalMatches += 1
            position += 1
        return totalMatches