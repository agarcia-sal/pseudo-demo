from collections import Counter

class Solution:
    def getSum(self, nums):
        modValue = 10**9 + 7

        def calc(nums):
            lengthVal = len(nums)
            arrayA = [0] * lengthVal
            arrayB = [0] * lengthVal
            frequencyMap = Counter()
            indexVar = 1
            while indexVar < lengthVal:
                prevNum = nums[indexVar - 1]
                additionVal = 1
                if prevNum in frequencyMap:
                    additionVal += frequencyMap[prevNum]
                frequencyMap[prevNum] = additionVal
                arrayA[indexVar] = frequencyMap[prevNum]
                indexVar += 1

            frequencyMap = Counter()
            idx = lengthVal - 2
            while idx >= 0:
                nextNum = nums[idx + 1]
                incrementVal = 1
                if nextNum in frequencyMap:
                    incrementVal += frequencyMap[nextNum]
                frequencyMap[nextNum] = incrementVal
                arrayB[idx] = frequencyMap[nextNum]
                idx -= 1

            accumulator = 0
            for i in range(lengthVal):
                longTermSum = arrayA[i] + arrayB[i] + (arrayA[i] * arrayB[i])
                contribution = longTermSum * nums[i]
                accumulator += contribution

            return accumulator % modValue

        firstCalc = calc(nums)
        nums.reverse()
        secondCalc = calc(nums)
        sumTotal = firstCalc + secondCalc
        sumElements = sum(nums)
        return (sumTotal + sumElements) % modValue