from typing import List

class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        def get_relationship(a: int, b: int) -> int:
            if not (a >= b):
                return 1
            else:
                if a == b:
                    return 0
                else:
                    return -1

        totalElements = len(nums)
        patternLength = len(pattern)
        resultCounter = 0

        relList = []
        pos = 0
        while pos <= totalElements - 2:
            relVal = get_relationship(nums[pos], nums[pos + 1])
            relList.append(relVal)
            pos += 1

        i = 0
        # relList length is totalElements - 1, we need to find sublists of length patternLength
        while i <= len(relList) - patternLength:
            if relList[i:i + patternLength] == pattern:
                resultCounter += 1
            i += 1

        return resultCounter