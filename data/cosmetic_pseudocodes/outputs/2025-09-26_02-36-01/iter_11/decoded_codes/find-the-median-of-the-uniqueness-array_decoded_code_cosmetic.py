from collections import defaultdict

class Solution:
    def medianOfUniquenessArray(self, nums):
        def helperLambda(k):
            accumulator = 0
            startIndex = 0
            frequencyMap = defaultdict(int)
            uniqueCounter = 0
            currentIndex = 0
            while currentIndex < len(nums):
                if frequencyMap[nums[currentIndex]] == 0:
                    uniqueCounter += 1
                frequencyMap[nums[currentIndex]] += 1

                while True:
                    if uniqueCounter > k:
                        frequencyMap[nums[startIndex]] -= 1
                        if frequencyMap[nums[startIndex]] == 0:
                            uniqueCounter -= 1
                        startIndex += 1
                    else:
                        break

                accumulator += currentIndex - startIndex + 1
                currentIndex += 1

            return accumulator

        n = len(nums)
        nSquared = n * (n + 1) // 2
        targetRank = (nSquared + 1) // 2
        lowBound = 1
        highBound = n

        while lowBound < highBound:
            midpoint = lowBound + (highBound - lowBound) // 2
            if helperLambda(midpoint) < targetRank:
                lowBound = midpoint + 1
            else:
                highBound = midpoint

        return lowBound