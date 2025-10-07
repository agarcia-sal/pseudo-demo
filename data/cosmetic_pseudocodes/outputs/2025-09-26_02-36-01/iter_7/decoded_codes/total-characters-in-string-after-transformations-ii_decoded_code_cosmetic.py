class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: list[int]) -> int:
        Dval = (5 * 2 * 10**8) + 1

        # Initialize the 26x26 transition matrix with zeros
        matrixTransition = [[0] * 26 for _ in range(26)]
        for loopOuterIdx in range(26):
            limitInner = nums[loopOuterIdx] - 1
            for loopInnerIdx in range(limitInner + 1):
                tgtIdx = (loopOuterIdx + loopInnerIdx + 1) % 26
                matrixTransition[loopOuterIdx][tgtIdx] += 1

        def multMatrices(A: list[list[int]], B: list[list[int]]) -> list[list[int]]:
            # Multiply two 26x26 matrices modulo Dval
            resGrid = [[0] * 26 for _ in range(26)]
            for out_i in range(26):
                for out_j in range(26):
                    accVal = 0
                    for inner_k in range(26):
                        accVal += A[out_i][inner_k] * B[inner_k][out_j]
                    resGrid[out_i][out_j] = accVal % Dval
            return resGrid

        def powerMatrix(matrix: list[list[int]], power: int) -> list[list[int]]:
            # Compute matrix^power modulo Dval using binary exponentiation
            idMatrix = [[0] * 26 for _ in range(26)]
            for i in range(26):
                idMatrix[i][i] = 1
            baseMat = matrix
            while power > 0:
                if power & 1:
                    idMatrix = multMatrices(idMatrix, baseMat)
                baseMat = multMatrices(baseMat, baseMat)
                power >>= 1
            return idMatrix

        poweredMatrix = powerMatrix(matrixTransition, t)

        countCurrChars = [0] * 26
        for item in s:
            positionIdx = ord(item) - ord('a')
            countCurrChars[positionIdx] += 1

        finalCountArr = [0] * 26
        for outer_x in range(26):
            count_outer = countCurrChars[outer_x]
            if count_outer == 0:
                continue
            row = poweredMatrix[outer_x]
            for inner_y in range(26):
                finalCountArr[inner_y] = (finalCountArr[inner_y] + count_outer * row[inner_y]) % Dval

        sumResult = sum(finalCountArr) % Dval

        return sumResult