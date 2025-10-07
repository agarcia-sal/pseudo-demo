from typing import List

class Solution:
    def countMatchingSubarrays(self, nums: List[int], pattern: List[int]) -> int:
        def get_relationship(numA: int, numB: int) -> int:
            if numA < numB:
                return 1
            elif numA == numB:
                return 0
            else:
                return -1

        lengthNums = len(nums)
        lengthPattern = len(pattern)
        matches = 0

        diffs = []
        for i in range(lengthNums - 1):
            diffs.append(get_relationship(nums[i], nums[i + 1]))

        for j in range(lengthNums - lengthPattern):
            if diffs[j:j + lengthPattern] == pattern:
                matches += 1

        return matches