from collections import defaultdict
from typing import List

class Solution:
    def maximumLength(self, nums: List[int], k: int) -> int:
        lenNums = len(nums)
        dpMatrix = [[0] * (k + 1) for _ in range(lenNums)]
        dictList = [defaultdict(int) for _ in range(k + 1)]
        bestThree = [[0, 0, 0] for _ in range(k + 1)]
        maxResult = 0

        def updateBest(groupIndex: int, currentVal: int, currentNum: int) -> None:
            # Update the top three best values for a group, maintaining the highest and second highest for different nums
            if bestThree[groupIndex][0] != currentNum:
                if currentVal >= bestThree[groupIndex][1]:
                    bestThree[groupIndex][2] = bestThree[groupIndex][1]
                    bestThree[groupIndex][1] = currentVal
                    bestThree[groupIndex][0] = currentNum
                else:
                    bestThree[groupIndex][2] = max(bestThree[groupIndex][2], currentVal)
            else:
                bestThree[groupIndex][1] = max(bestThree[groupIndex][1], currentVal)

        def processIndex(currentIndex: int) -> None:
            nonlocal maxResult
            numAtIndex = nums[currentIndex]
            groupCounter = 0

            while True:
                if groupCounter > k:
                    break

                dpMatrix[currentIndex][groupCounter] = dictList[groupCounter].get(numAtIndex, 0)

                if groupCounter > 0:
                    if bestThree[groupCounter - 1][0] != numAtIndex:
                        dpMatrix[currentIndex][groupCounter] = max(dpMatrix[currentIndex][groupCounter],
                                                                  bestThree[groupCounter - 1][1])
                    else:
                        dpMatrix[currentIndex][groupCounter] = max(dpMatrix[currentIndex][groupCounter],
                                                                  bestThree[groupCounter - 1][2])

                dpMatrix[currentIndex][groupCounter] += 1
                dictList[groupCounter][numAtIndex] = max(dictList[groupCounter].get(numAtIndex, 0),
                                                        dpMatrix[currentIndex][groupCounter])
                updateBest(groupCounter, dpMatrix[currentIndex][groupCounter], numAtIndex)
                maxResult = max(maxResult, dpMatrix[currentIndex][groupCounter])
                groupCounter += 1

        if lenNums > 0:
            for currIdx in range(lenNums):
                processIndex(currIdx)

        return maxResult