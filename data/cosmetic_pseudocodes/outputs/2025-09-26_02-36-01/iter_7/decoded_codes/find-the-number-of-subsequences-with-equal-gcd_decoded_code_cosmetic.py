class Solution:
    def subsequencePairCount(self, nums):
        MODULO_VALUE = 10 * (10 ** 8) + 7

        # Find the maximum number in nums to determine matrix dimensions
        upperBound = float('-inf')
        for num in nums:
            if num > upperBound:
                upperBound = num

        matrixDim = upperBound + 1  # upperBound + (2 - 1) = upperBound + 1

        # Initialize DP matrix with zeros
        prevMatrix = [[0] * (matrixDim + 1) for _ in range(matrixDim + 1)]
        prevMatrix[0][0] = 1  # base case

        def RecGCD(a, b):
            while b != 0:
                a, b = b, a % b
            return a

        def PROCESS_NEXT_NUM(currentNum, currentDp):
            tempDp = [[0] * (matrixDim + 1) for _ in range(matrixDim + 1)]
            for rowCtr in range(matrixDim + 1):
                for colCtr in range(matrixDim + 1):
                    val = currentDp[rowCtr][colCtr] % MODULO_VALUE
                    if val == 0:
                        continue
                    # Keep subsequence unchanged
                    tempDp[rowCtr][colCtr] = (tempDp[rowCtr][colCtr] + val) % MODULO_VALUE

                    # Update row index gcd with currentNum
                    gX = RecGCD(rowCtr, currentNum)
                    tempDp[gX][colCtr] = (tempDp[gX][colCtr] + val) % MODULO_VALUE

                    # Update col index gcd with currentNum
                    gY = RecGCD(colCtr, currentNum)
                    tempDp[rowCtr][gY] = (tempDp[rowCtr][gY] + val) % MODULO_VALUE

            return tempDp

        for num in nums:
            prevMatrix = PROCESS_NEXT_NUM(num, prevMatrix)

        finalRes = 0
        for gIdx in range(1, upperBound + 1):
            finalRes = (finalRes + prevMatrix[gIdx][gIdx]) % MODULO_VALUE

        return finalRes