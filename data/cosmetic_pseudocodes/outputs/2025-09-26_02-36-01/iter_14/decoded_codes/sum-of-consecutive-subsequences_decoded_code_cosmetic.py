from collections import Counter
from typing import List

class Solution:
    def getSum(self, nums: List[int]) -> int:
        def calc(numbers: List[int]) -> int:
            lengthVal = len(numbers)
            prefixCounts = [0] * lengthVal
            suffixCounts = [0] * lengthVal
            frequencyMap = Counter()

            indexA = 1
            while indexA < lengthVal:
                prevNum = numbers[indexA - 1]
                freqBefore = frequencyMap[prevNum] if prevNum in frequencyMap else 0
                frequencyMap[prevNum] = freqBefore + 1
                prefixCounts[indexA] = frequencyMap[prevNum]
                indexA += 1

            frequencyMap = Counter()
            indexB = lengthVal - 2
            while indexB >= 0:
                nextNum = numbers[indexB + 1]
                freqAfter = frequencyMap[nextNum] if nextNum in frequencyMap else 0
                frequencyMap[nextNum] = freqAfter + 1
                suffixCounts[indexB] = frequencyMap[nextNum]
                indexB -= 1

            aggregateSum = 0
            idxC = 0
            MOD = 10**9 + 7
            while True:
                if idxC >= lengthVal:
                    break
                leftVal = prefixCounts[idxC]
                rightVal = suffixCounts[idxC]
                currentNum = numbers[idxC]
                tempSum = currentNum * (leftVal + rightVal + (leftVal * rightVal))
                aggregateSum += tempSum
                idxC += 1

            return aggregateSum % MOD

        MODULO_CONST = 10**9 + 7
        firstCalc = calc(nums)
        self.reverseArray(nums)
        secondCalc = calc(nums)

        sumVals = 0
        iteratorPos = 0
        lengthNums = len(nums)
        while True:
            if iteratorPos >= lengthNums:
                break
            sumVals += nums[iteratorPos]
            iteratorPos += 1

        return (firstCalc + secondCalc + sumVals) % MODULO_CONST

    def reverseArray(self, arr: List[int]) -> None:
        startIdx = 0
        endIdx = len(arr) - 1
        while startIdx < endIdx:
            tempVal = arr[startIdx]
            arr[startIdx] = arr[endIdx]
            arr[endIdx] = tempVal
            startIdx += 1
            endIdx -= 1