from collections import defaultdict

class Solution:
    def medianOfUniquenessArray(self, nums):
        def countLessOrEqual(target):
            counts = defaultdict(int)
            leftIndex = 0
            uniqueCount = 0
            result = 0
            for rightIndex, num in enumerate(nums):
                if counts[num] == 0:
                    uniqueCount += 1
                counts[num] += 1
                while uniqueCount > target:
                    counts[nums[leftIndex]] -= 1
                    if counts[nums[leftIndex]] == 0:
                        uniqueCount -= 1
                    leftIndex += 1
                result += rightIndex - leftIndex + 1
            return result

        n = len(nums)
        totalSubarrays = n * (n + 1) // 2
        medianTarget = (totalSubarrays + 1) // 2
        start, end = 1, n
        while start < end:
            midVal = (start + end) // 2
            if countLessOrEqual(midVal) < medianTarget:
                start = midVal + 1
            else:
                end = midVal
        return start