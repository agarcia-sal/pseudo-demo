from collections import Counter
from math import comb

class Solution:
    def gcdValues(self, nums, queries):
        # Convert nums and queries to 0-based indexing internally
        # but since pseudocode uses 1-based indexing, we just adjust accordingly.
        # nums and queries are lists of integers.

        # Find max value in nums
        def maxOfList(inputList):
            tempMaxVar = inputList[0]
            for idx in range(1, len(inputList)):
                if inputList[idx] > tempMaxVar:
                    tempMaxVar = inputList[idx]
            return tempMaxVar

        upperBound = maxOfList(nums)

        # Count occurrences of each number in nums
        def countOccurrences(dataList):
            counterDict = {}
            scanIndex = 0
            while scanIndex < len(dataList):
                currentElem = dataList[scanIndex]
                if currentElem in counterDict:
                    counterDict[currentElem] = counterDict[currentElem] + 1
                else:
                    counterDict[currentElem] = 1
                scanIndex += 1
            return counterDict

        frequencyMap = countOccurrences(nums)

        # Create zero-initialized list of size upperBound+1 (for 1-based indexing convenience)
        def createZeroList(sizeVal):
            container = [0]*(sizeVal+1)
            return container

        gcdNumberList = createZeroList(upperBound)

        decreasingIndex = upperBound
        while decreasingIndex >= 1:
            innerSum = 0
            innerIndex = decreasingIndex
            while innerIndex <= upperBound:
                if innerIndex in frequencyMap:
                    innerSum += frequencyMap[innerIndex]
                gcdNumberList[decreasingIndex] -= gcdNumberList[innerIndex]
                innerIndex += decreasingIndex
            tempValA = (innerSum * (innerSum - 1)) // 2  # integer division
            gcdNumberList[decreasingIndex] += tempValA
            decreasingIndex -= 1

        # accumulateList function: prefix sums of gcdNumberList
        def accumulateList(values):
            resultList = [0]*(len(values))
            runningTotal = 0
            positionCounter = 1
            while positionCounter < len(values):
                runningTotal += values[positionCounter]
                resultList[positionCounter] = runningTotal
                positionCounter += 1
            return resultList

        cumulativeSum = accumulateList(gcdNumberList)

        outputCollection = []
        queryPosition = 0
        while queryPosition < len(queries):
            target = queries[queryPosition]

            lowBound = 0
            highBound = len(cumulativeSum)-1
            finalIndex = 0

            while lowBound < highBound:
                midPoint = (lowBound + highBound) // 2
                if cumulativeSum[midPoint+1] > target:
                    highBound = midPoint
                else:
                    lowBound = midPoint + 1
            finalIndex = lowBound + 1
            outputCollection.append(finalIndex)
            queryPosition += 1

        return outputCollection