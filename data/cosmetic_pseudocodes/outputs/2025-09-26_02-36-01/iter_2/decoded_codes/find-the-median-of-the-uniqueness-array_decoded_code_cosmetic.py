from collections import defaultdict

class Solution:
    def medianOfUniquenessArray(self, nums):
        def countLessOrEqual(threshold):
            accumulator = 0
            windowStart = 0
            frequencyMap = defaultdict(int)
            uniqueCounter = 0

            for index, num in enumerate(nums):
                if frequencyMap[num] == 0:
                    uniqueCounter += 1
                frequencyMap[num] += 1

                while uniqueCounter > threshold:
                    frequencyMap[nums[windowStart]] -= 1
                    if frequencyMap[nums[windowStart]] == 0:
                        uniqueCounter -= 1
                    windowStart += 1

                accumulator += (index - windowStart + 1)

            return accumulator

        n = len(nums)
        totalSubarrays = n * (n + 1) // 2
        medianTarget = (totalSubarrays + 1) // 2
        start, end = 1, n

        while start < end:
            middle = start + (end - start) // 2
            if countLessOrEqual(middle) < medianTarget:
                start = middle + 1
            else:
                end = middle

        return start