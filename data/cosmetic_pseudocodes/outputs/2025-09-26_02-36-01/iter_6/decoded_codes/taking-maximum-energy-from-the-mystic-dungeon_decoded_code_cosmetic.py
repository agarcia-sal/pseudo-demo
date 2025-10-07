from collections import deque
from typing import List

class Solution:
    def maximumEnergy(self, batteryLevels: List[int], limit: int) -> int:
        totalCount = len(batteryLevels)
        memoization = [0] * totalCount
        lastIndex = totalCount - 1
        memoization[lastIndex] = batteryLevels[lastIndex]
        highestValue = memoization[lastIndex]

        def checkFrontThreshold(dequeList: deque, currentIndex: int, thresholdLimit: int) -> bool:
            if not dequeList:
                return False
            frontIndex = dequeList[0]
            return (frontIndex - currentIndex) >= thresholdLimit

        def popFront(dequeList: deque) -> None:
            if dequeList:
                dequeList.popleft()

        def popBack(dequeList: deque) -> None:
            if dequeList:
                dequeList.pop()

        indicesQueue = deque()
        indicesQueue.append(lastIndex)
        iterator = lastIndex - 1

        while iterator >= 0:
            while checkFrontThreshold(indicesQueue, iterator, limit):
                popFront(indicesQueue)

            frontElement = indicesQueue[0]
            partialSum = batteryLevels[iterator] + memoization[frontElement]
            memoization[iterator] = partialSum

            if highestValue < memoization[iterator]:
                highestValue = memoization[iterator]

            while indicesQueue and memoization[iterator] >= memoization[indicesQueue[-1]]:
                popBack(indicesQueue)

            indicesQueue.append(iterator)
            iterator -= 1

        return highestValue