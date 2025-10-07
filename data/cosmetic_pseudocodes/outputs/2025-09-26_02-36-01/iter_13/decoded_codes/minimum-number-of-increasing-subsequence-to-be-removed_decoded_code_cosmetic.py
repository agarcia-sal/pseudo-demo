from typing import List

class Solution:
    def minOperations(self, inputList: List[int]) -> int:
        def maxValue(a: int, b: int) -> int:
            return a if a >= b else b

        lengthValue = len(inputList)
        if lengthValue == 0:
            return 0

        dpList = [1] * lengthValue

        def innerLoop(j: int, i: int, nums: List[int], dp: List[int]) -> None:
            if j < 0:
                return
            if nums[i] <= nums[j]:
                dp[i] = maxValue(dp[i], dp[j] + 1)
            innerLoop(j - 1, i, nums, dp)

        idxOuter = 1
        while idxOuter < lengthValue:
            idxInner = idxOuter - 1
            innerLoop(idxInner, idxOuter, inputList, dpList)
            idxOuter += 1

        currentMax = dpList[0]
        idxOuter = 1
        while idxOuter < lengthValue:
            currentMax = maxValue(currentMax, dpList[idxOuter])
            idxOuter += 1

        return currentMax