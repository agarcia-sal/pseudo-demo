from typing import List

class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        def checkSequence(startIndex: int, sequence: List[int]) -> bool:
            for idx1 in range(len(sequence) - 1):
                current = nums[startIndex + idx1]
                next_val = nums[startIndex + idx1 + 1]
                cond = sequence[idx1]
                if cond == 1:
                    if not (current < next_val):
                        return False
                elif cond == 0:
                    if current != next_val:
                        return False
                elif cond == -1:
                    if not (current > next_val):
                        return False
                else:
                    # If the pattern contains other values, fail safe as pattern only expects -1,0,1
                    return False
            return True

        lenNums = len(nums)
        lenPattern = len(pattern)
        totalMatches = 0
        start = 0

        while start <= lenNums - lenPattern:
            if checkSequence(start, pattern):
                totalMatches += 1
            start += 1

        return totalMatches