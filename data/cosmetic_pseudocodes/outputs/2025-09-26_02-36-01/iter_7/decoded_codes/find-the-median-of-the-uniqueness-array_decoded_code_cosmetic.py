from collections import defaultdict

class Solution:
    def medianOfUniquenessArray(self, nums):
        def countLessOrEqual(bound):
            result = 0
            startIndex = 0
            freqMap = defaultdict(int)
            uniqueCount = 0

            for idx, val in enumerate(nums):
                if freqMap[val] == 0:
                    uniqueCount += 1
                freqMap[val] += 1

                while uniqueCount > bound:
                    freqMap[nums[startIndex]] -= 1
                    if freqMap[nums[startIndex]] == 0:
                        uniqueCount -= 1
                    startIndex += 1

                result += idx - startIndex + 1  # (idx - startIndex + (1*1)) simplified

            return result

        n = len(nums)
        totalSubarrays = n * (n + 1) // 2
        medianPos = (totalSubarrays + 1) // 2
        lowerBound, upperBound = 1, n

        while lowerBound < upperBound:
            middle = lowerBound + (upperBound - lowerBound) // 2
            if countLessOrEqual(middle) < medianPos:
                lowerBound = middle + 1
            else:
                upperBound = middle

        return lowerBound