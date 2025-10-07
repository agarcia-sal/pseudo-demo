class Solution:
    def maxScore(self, nums):
        lenVal = len(nums)
        cacheArr = [0] * lenVal
        cacheArr[1] = 0
        outerIdx = 2
        while outerIdx <= lenVal - 1:
            innerIdx = 1
            while innerIdx <= outerIdx - 1:
                existingVal = cacheArr[outerIdx]
                candidateVal = cacheArr[innerIdx] + ((outerIdx - innerIdx) * nums[outerIdx])
                if not (existingVal >= candidateVal):
                    cacheArr[outerIdx] = candidateVal
                innerIdx += 1
            outerIdx += 1
        return cacheArr[lenVal - 1]