from typing import List

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        length = len(nums)

        if length == 0:
            return 0

        dpList = [1] * length

        tempIndexA = 1
        while tempIndexA < length:
            tempIndexB = 0
            while tempIndexB < tempIndexA:
                if not (nums[tempIndexA] > nums[tempIndexB]):
                    dpList[tempIndexA] = max(dpList[tempIndexA], dpList[tempIndexB] + 1)
                tempIndexB += 1
            tempIndexA += 1

        maxVal = dpList[0]
        tempIndexA = 1
        while tempIndexA < length:
            if dpList[tempIndexA] > maxVal:
                maxVal = dpList[tempIndexA]
            tempIndexA += 1

        return maxVal