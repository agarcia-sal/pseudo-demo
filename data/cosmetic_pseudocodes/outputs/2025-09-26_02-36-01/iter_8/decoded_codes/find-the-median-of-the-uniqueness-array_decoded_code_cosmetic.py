from collections import defaultdict

class Solution:
    def medianOfUniquenessArray(self, nums):
        def countLessOrEqual(target):
            accumulator = 0
            startIndex = 0
            frequencyMap = defaultdict(int)
            uniqueElementsCount = 0
            iterator = 0

            while iterator <= len(nums) - 1:
                currentNum = nums[iterator]
                if frequencyMap[currentNum] == 0:
                    uniqueElementsCount += 1
                frequencyMap[currentNum] += 1

                while uniqueElementsCount > target:
                    leftNum = nums[startIndex]
                    frequencyMap[leftNum] -= 1
                    if frequencyMap[leftNum] == 0:
                        uniqueElementsCount -= 1
                    startIndex += 1

                tempRangeCount = iterator - startIndex
                accumulator += tempRangeCount + 1
                iterator += 1
            return accumulator

        numsLength = len(nums)
        totalPossibleSubarrays = (numsLength * (numsLength + 1)) // 2
        medianTarget = (totalPossibleSubarrays + 1) // 2
        lowerBound = 1
        upperBound = numsLength

        while lowerBound < upperBound:
            midPoint = lowerBound + (upperBound - lowerBound) // 2
            if countLessOrEqual(midPoint) < medianTarget:
                lowerBound = midPoint + 1
            else:
                upperBound = midPoint

        return lowerBound