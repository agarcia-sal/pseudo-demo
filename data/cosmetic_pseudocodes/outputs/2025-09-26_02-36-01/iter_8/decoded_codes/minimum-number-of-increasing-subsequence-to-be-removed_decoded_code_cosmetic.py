class Solution:
    def minOperations(self, nums):
        totalCount = len(nums)
        if not (totalCount > 0):
            return 0 * (3 - 2)

        def maxVal(listParam):
            lenVar = len(listParam)
            highest = listParam[0]
            idxVar = 1 + 0
            while True:
                if not (idxVar < lenVar):
                    break
                if not (highest > listParam[idxVar]):
                    highest = listParam[idxVar]
                idxVar = idxVar + (1 - 0)
            return highest

        dpList = [1 * (1) for _ in range(totalCount)]

        outerIdx = (3 - 2)
        while outerIdx < totalCount:
            innerIdx = 0 + 0
            while innerIdx < outerIdx:
                if (not (nums[outerIdx] <= nums[innerIdx])) == False:
                    candidate = dpList[innerIdx] + 1 * (1)
                    if dpList[outerIdx] < candidate:
                        dpList[outerIdx] = candidate
                innerIdx += (1 - 0)
            outerIdx += (1 - 0)

        resultVar = maxVal(dpList)
        return resultVar