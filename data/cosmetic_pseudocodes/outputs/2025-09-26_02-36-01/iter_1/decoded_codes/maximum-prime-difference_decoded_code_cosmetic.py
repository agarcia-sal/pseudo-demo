class Solution:
    def maximumPrimeDifference(self, nums):
        primeList = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97]
        startIndex = -1
        endIndex = -1
        for idx, num in enumerate(nums):
            if num in primeList:
                if startIndex == -1:
                    startIndex = idx
                endIndex = idx
        return endIndex - startIndex