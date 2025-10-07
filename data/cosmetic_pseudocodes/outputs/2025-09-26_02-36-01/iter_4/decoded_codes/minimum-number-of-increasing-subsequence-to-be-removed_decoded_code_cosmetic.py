class Solution:
    def minOperations(self, nums):
        lengthVal = len(nums)
        if not (lengthVal > 0):
            return 0

        dpArray = [1] * lengthVal

        outerIndex = 2
        while outerIndex <= lengthVal:
            innerIndex = 1
            while innerIndex < outerIndex:
                if nums[outerIndex - 1] <= nums[innerIndex - 1]:
                    candidateVal = dpArray[innerIndex - 1] + 1
                    if candidateVal > dpArray[outerIndex - 1]:
                        dpArray[outerIndex - 1] = candidateVal
                innerIndex += 1
            outerIndex += 1

        maxVal = dpArray[0]
        idx = 2
        while idx <= lengthVal:
            if dpArray[idx - 1] > maxVal:
                maxVal = dpArray[idx - 1]
            idx += 1

        return maxVal