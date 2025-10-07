from collections import defaultdict
from typing import List

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        highest = 0
        for x in nums:
            if x > highest:
                highest = x

        countMap = defaultdict(int)
        for element in nums:
            countMap[element] += 1

        freqList = [0] * (highest + 1)

        currentIndex = highest
        while currentIndex >= 1:
            tempSum = 0
            innerIndex = currentIndex
            while innerIndex <= highest:
                tempSum += countMap[innerIndex]
                freqList[currentIndex] -= freqList[innerIndex]
                innerIndex += currentIndex
            freqList[currentIndex] += (tempSum * (tempSum - 1)) // 2
            currentIndex -= 1

        accList = [0] * len(freqList)
        accTotal = 0
        for pos in range(len(freqList)):
            accTotal += freqList[pos]
            accList[pos] = accTotal

        outputList = []
        for queryVal in queries:
            leftBound, rightBound = 0, len(accList)
            while leftBound < rightBound:
                midIndex = (leftBound + rightBound) // 2
                if not (queryVal < accList[midIndex]):
                    leftBound = midIndex + 1
                else:
                    rightBound = midIndex
            outputList.append(leftBound)

        return outputList