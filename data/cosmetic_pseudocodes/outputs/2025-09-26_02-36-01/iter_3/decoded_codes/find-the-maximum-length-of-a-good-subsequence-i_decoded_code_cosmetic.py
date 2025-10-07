class Solution:
    def maximumLength(self, nums, k):
        lengthNums = len(nums)
        matrixF = [[1] * (k + 1) for _ in range(lengthNums)]
        maxResult = 0

        for outerIndex in range(lengthNums):
            currentVal = nums[outerIndex]
            for hValue in range(k + 1):
                for innerIndex in range(outerIndex):
                    priorVal = nums[innerIndex]
                    if currentVal == priorVal:
                        candidateVal = matrixF[innerIndex][hValue] + 1
                        if candidateVal > matrixF[outerIndex][hValue]:
                            matrixF[outerIndex][hValue] = candidateVal
                    else:
                        if hValue > 0:
                            candidateVal = matrixF[innerIndex][hValue - 1] + 1
                            if candidateVal > matrixF[outerIndex][hValue]:
                                matrixF[outerIndex][hValue] = candidateVal
            if maxResult < matrixF[outerIndex][k]:
                maxResult = matrixF[outerIndex][k]
        return maxResult