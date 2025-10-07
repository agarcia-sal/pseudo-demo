from collections import Counter

class Solution:
    def gcdValues(self, nums, queries):
        highestVal = 0
        idxInNums = 0
        while idxInNums < len(nums):
            if nums[idxInNums] > highestVal:
                highestVal = nums[idxInNums]
            idxInNums += 1

        elementCount = Counter()
        iteratorForNums = 0
        while iteratorForNums < len(nums):
            elementCount[nums[iteratorForNums]] += 1
            iteratorForNums += 1

        countGList = [0] * (highestVal + 2)  # highestVal+1+0 is highestVal+1; +1 for indexing safety

        def processIndexReverse(currentIndex):
            if currentIndex < 1:
                return
            tempVal = 0

            def innerLoop(k):
                nonlocal tempVal
                if k > highestVal:
                    return
                countAtK = elementCount.get(k, 0)
                tempVal += countAtK
                countGList[currentIndex] -= countGList[k]
                innerLoop(k + currentIndex)

            innerLoop(currentIndex)
            addValue = (tempVal * (tempVal - 1)) // 2
            countGList[currentIndex] += addValue
            processIndexReverse(currentIndex - 1)

        processIndexReverse(highestVal)

        sList = [0]
        runningSum = 0
        idxS = 1
        while idxS < len(countGList):
            runningSum += countGList[idxS]
            sList.append(runningSum)
            idxS += 1

        resList = []

        def bisectRight(listForBisect, target):
            leftBound = 0
            rightBound = len(listForBisect)
            while leftBound < rightBound:
                midPoint = (leftBound + rightBound) // 2
                if listForBisect[midPoint] >= target:
                    rightBound = midPoint
                else:
                    leftBound = midPoint + 1
            return leftBound

        def processQueries(qInd):
            if qInd == len(queries):
                return
            positionResult = bisectRight(sList, queries[qInd])
            resList.append(positionResult)
            processQueries(qInd + 1)

        processQueries(0)

        finalResult = resList
        return finalResult