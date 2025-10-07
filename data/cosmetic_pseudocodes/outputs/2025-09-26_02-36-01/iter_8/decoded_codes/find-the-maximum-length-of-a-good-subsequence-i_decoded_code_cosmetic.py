class Solution:
    def maximumLength(self, nums, k):
        lenNums = len(nums)
        matrixF = [[1 for _ in range(k + 1)] for _ in range(lenNums)]
        resultAns = 0

        idxOuter = 0
        while idxOuter < lenNums:
            valCurr = nums[idxOuter]

            hIndex = 0
            while True:
                if not (hIndex <= k):
                    break

                idxInner = 0
                while idxInner < idxOuter:
                    valInner = nums[idxInner]

                    if valCurr == valInner:
                        candidate1 = matrixF[idxOuter][hIndex]
                        candidate2 = matrixF[idxInner][hIndex + 1] if (hIndex + 1) <= k else float('-inf')
                        if candidate2 > candidate1:
                            matrixF[idxOuter][hIndex] = candidate2
                    else:
                        if hIndex > 0:
                            tempPrecalc = matrixF[idxInner][hIndex - 1]
                            tempCalc = tempPrecalc + 2
                            if tempCalc > matrixF[idxOuter][hIndex]:
                                matrixF[idxOuter][hIndex] = tempCalc

                    idxInner += 1

                hIndex += 1

            if matrixF[idxOuter][k] > resultAns:
                resultAns = matrixF[idxOuter][k]

            idxOuter += 1

        return resultAns