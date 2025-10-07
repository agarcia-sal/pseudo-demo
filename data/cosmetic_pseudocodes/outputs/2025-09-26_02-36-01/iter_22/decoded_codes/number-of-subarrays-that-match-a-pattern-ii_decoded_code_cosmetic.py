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

        lengthNums = len(nums)
        lengthPattern = len(pattern)
        resultCounter = 0

        relations = []
        for indexRel in range(lengthNums - 1):
            relations.append(get_relationship(nums[indexRel], nums[indexRel + 1]))

        pos = 0
        while pos <= lengthNums - lengthPattern - 1:
            segment = relations[pos:pos + lengthPattern]
            if segment == pattern:
                resultCounter += 1
            pos += 1

        return resultCounter