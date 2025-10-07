class Solution:
    def maximumSubarrayXor(self, nums, queries):
        lengthVars = len(nums) - 1
        size = lengthVars + 1

        # Initialize 2D arrays matAlpha and matBeta with zeros
        matAlpha = [[0] * size for _ in range(size)]
        matBeta = [[0] * size for _ in range(size)]

        idxOuter = lengthVars
        while idxOuter >= 0:
            rowCol = idxOuter
            matAlpha[rowCol][rowCol] = nums[rowCol]
            matBeta[rowCol][rowCol] = nums[rowCol]

            idxInner = rowCol + 1
            while idxInner <= lengthVars:
                matAlpha[rowCol][idxInner] = matAlpha[rowCol][idxInner - 1] ^ matAlpha[rowCol + 1][idxInner]

                elementsForMax = [
                    matAlpha[rowCol][idxInner],
                    matBeta[rowCol][idxInner - 1],
                    matBeta[rowCol + 1][idxInner]
                ]

                currentMax = elementsForMax[0]
                for idxTempToCheck in range(1, len(elementsForMax)):
                    if elementsForMax[idxTempToCheck] > currentMax:
                        currentMax = elementsForMax[idxTempToCheck]

                matBeta[rowCol][idxInner] = currentMax
                idxInner += 1

            idxOuter -= 1

        outputList = []
        for leftIdx, rightIdx in queries:
            outputList.append(matBeta[leftIdx][rightIdx])

        return outputList