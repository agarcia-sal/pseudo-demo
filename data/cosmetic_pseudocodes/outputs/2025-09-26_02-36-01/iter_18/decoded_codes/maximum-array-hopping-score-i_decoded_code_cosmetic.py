class Solution:
    def maxScore(self, nums):
        totalElements = len(nums)
        cacheList = [0] * totalElements
        indexVar = 1
        while indexVar < totalElements:
            innerIndex = 0
            while innerIndex < indexVar:
                candidate = cacheList[innerIndex] + (indexVar - innerIndex) * nums[indexVar]
                if cacheList[indexVar] < candidate:
                    cacheList[indexVar] = candidate
                innerIndex += 1
            indexVar += 1
        resultVar = cacheList[totalElements - 1]
        return resultVar