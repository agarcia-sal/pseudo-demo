class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: list[int]) -> int:
        modVal = 1_000_000_000 + 1

        # Build the transformation matrix
        conversion = [[0] * 26 for _ in range(26)]
        for outerIndex in range(26):
            innerLimit = nums[outerIndex]
            for innerIndex in range(innerLimit):
                targetCol = (outerIndex + innerIndex + 1) % 26
                conversion[outerIndex][targetCol] += 1

        def matrix_multiply(A: list[list[int]], B: list[list[int]]) -> list[list[int]]:
            dimensions = 26
            output = [[0] * dimensions for _ in range(dimensions)]
            for outerI in range(dimensions):
                a_row = A[outerI]
                for outerJ in range(dimensions):
                    sumAcc = 0
                    for middleK in range(dimensions):
                        sumAcc += a_row[middleK] * B[middleK][outerJ]
                    output[outerI][outerJ] = sumAcc % modVal
            return output

        def matrix_power(matrix: list[list[int]], power: int) -> list[list[int]]:
            sizeMatrix = 26
            identity = [[1 if i == j else 0 for j in range(sizeMatrix)] for i in range(sizeMatrix)]
            baseMat = matrix
            exponent = power
            while exponent > 0:
                if exponent % 2 != 0:
                    identity = matrix_multiply(identity, baseMat)
                baseMat = matrix_multiply(baseMat, baseMat)
                exponent //= 2
            return identity

        raisedMatrix = matrix_power(conversion, t)

        freqArr = [0] * 26
        for ch in s:
            indexPos = ord(ch) - ord('a')
            freqArr[indexPos] += 1

        finalFreq = [0] * 26
        for outerP in range(26):
            freqVal = freqArr[outerP]
            row = raisedMatrix[outerP]
            for innerQ in range(26):
                partialValue = freqVal * row[innerQ]
                finalFreq[innerQ] = (finalFreq[innerQ] + partialValue) % modVal

        totalSum = sum(finalFreq) % modVal
        return totalSum