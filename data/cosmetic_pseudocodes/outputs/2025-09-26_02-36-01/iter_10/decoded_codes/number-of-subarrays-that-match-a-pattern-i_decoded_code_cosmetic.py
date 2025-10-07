from typing import List

class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        sizeNums = len(nums)
        sizePat = len(pattern)
        totalMatches = 0

        def isInvalidSegment(arr: List[int], idx: int, pat: List[int], pos: int) -> bool:
            # Check conditions based on pattern value at pos
            if pat[pos] == 1:
                return arr[idx + pos + 1] <= arr[idx + pos]
            elif pat[pos] == 0:
                return arr[idx + pos + 1] != arr[idx + pos]
            elif pat[pos] == -1:
                return arr[idx + pos + 1] >= arr[idx + pos]
            return False

        def verifyPattern(index: int, offset: int) -> bool:
            if offset >= sizePat - 1:
                return True
            if isInvalidSegment(nums, index, pattern, offset):
                return False
            return verifyPattern(index, offset + 1)

        def checkAtIndex(pos: int) -> bool:
            if pos > sizeNums - sizePat:
                return False
            return verifyPattern(pos, 0)

        def iterateOverPositions(current: int) -> None:
            nonlocal totalMatches
            if current > sizeNums - sizePat:
                return
            if checkAtIndex(current):
                totalMatches += 1
            iterateOverPositions(current + 1)

        iterateOverPositions(0)
        return totalMatches