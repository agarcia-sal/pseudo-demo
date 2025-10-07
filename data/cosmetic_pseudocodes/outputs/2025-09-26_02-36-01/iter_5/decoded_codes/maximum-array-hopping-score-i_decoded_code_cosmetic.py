from typing import List

class Solution:
    def maxScore(self, nums: List[int]) -> int:
        lengthVal = len(nums)
        dpArray = [0] * lengthVal

        def innerLoop(targetIndex: int, currentIndex: int, currentMax: int) -> int:
            if currentIndex >= targetIndex:
                return currentMax
            candidateScore = dpArray[currentIndex] + (targetIndex - currentIndex) * nums[targetIndex]
            updatedMax = currentMax
            if candidateScore > currentMax:
                updatedMax = candidateScore
            return innerLoop(targetIndex, currentIndex + 1, updatedMax)

        def outerLoop(i: int) -> None:
            if i >= lengthVal:
                return
            dpArray[i] = innerLoop(i, 0, 0)
            outerLoop(i + 1)

        outerLoop(1)
        resultValue = dpArray[lengthVal - 1]
        return resultValue