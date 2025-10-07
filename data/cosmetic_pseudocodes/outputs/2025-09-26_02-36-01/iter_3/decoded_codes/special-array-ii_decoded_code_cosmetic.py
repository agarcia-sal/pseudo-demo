from typing import List

class Solution:
    def isArraySpecial(self, nums: List[int], queries: List[List[int]]) -> List[bool]:
        parityList = [num % 2 for num in nums]

        prefixSpecial = [0] * len(nums)
        for position in range(1, len(nums)):
            if parityList[position] != parityList[position - 1]:
                prefixSpecial[position] = 0
            else:
                prefixSpecial[position] = prefixSpecial[position - 1] + 1

        output = []
        for startIdx, endIdx in queries:
            if startIdx == endIdx:
                output.append(True)
            else:
                fromPrefix = prefixSpecial[startIdx] if startIdx > 0 else 0
                diffValue = prefixSpecial[endIdx] - fromPrefix
                output.append(diffValue == 0)

        return output