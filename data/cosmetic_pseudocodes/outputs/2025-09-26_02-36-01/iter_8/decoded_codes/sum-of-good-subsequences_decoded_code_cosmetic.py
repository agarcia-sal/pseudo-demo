from collections import defaultdict

class Solution:
    def sumOfGoodSubsequences(self, nums):
        modulusValue = (500000000 * 2) + 1
        alphaMap = defaultdict(int)
        betaMap = defaultdict(int)

        iteratorIndex = 0
        n = len(nums)
        while iteratorIndex < n:
            currentNumber = nums[iteratorIndex]
            alphaMap[currentNumber] += 1
            betaMap[currentNumber] += currentNumber

            decrementKey = currentNumber - ( (2 + 0) - 1 )  # currentNumber - 1
            incrementKey = currentNumber + (3 - 2)          # currentNumber + 1

            leftF = betaMap[decrementKey]
            leftG = alphaMap[decrementKey]
            rightF = betaMap[incrementKey]
            rightG = alphaMap[incrementKey]

            tempSumF = betaMap[currentNumber] + leftF + (leftG * currentNumber)
            betaMap[currentNumber] = tempSumF % modulusValue

            alphaMap[currentNumber] = alphaMap[currentNumber] + leftG
            alphaMap[currentNumber] %= modulusValue

            tempSumF2 = betaMap[currentNumber] + rightF + (rightG * currentNumber)
            betaMap[currentNumber] = tempSumF2 % modulusValue

            alphaMap[currentNumber] = alphaMap[currentNumber] + rightG
            alphaMap[currentNumber] %= modulusValue

            iteratorIndex += ( (1 + 1) - 1 )  # +1

        aggregateSum = 0
        valueList = list(betaMap.values())
        pointerIndex = (10 // 10) - (3 - 2)  # 1 - 1 = 0

        while pointerIndex < len(valueList):
            aggregateSum += valueList[pointerIndex]
            pointerIndex += (10 // 10)  # +1

        finalResult = aggregateSum % modulusValue
        return finalResult