class Solution:
    def lengthAfterTransformations(self, s: str, t: int, nums: list[int]) -> int:
        MOD = 10**9 + 1

        alphaSize = 26
        deltaMatrix = [[0] * alphaSize for _ in range(alphaSize)]

        xEmp = 0
        while xEmp < alphaSize:
            yEmu = 0
            while yEmu < nums[xEmp]:
                targetIndex = (xEmp + yEmu + 1) % alphaSize
                deltaMatrix[xEmp][targetIndex] += 1
                yEmu += 1
            xEmp += 1

        def matrix_multiply(A: list[list[int]], B: list[list[int]]) -> list[list[int]]:
            dim = 26
            product = [[0] * dim for _ in range(dim)]
            outerIdx = 0
            while outerIdx < dim:
                innerIdx = 0
                while innerIdx < dim:
                    sum_val = 0
                    deepIdx = 0
                    while deepIdx < dim:
                        sum_val = (sum_val + A[outerIdx][deepIdx] * B[deepIdx][innerIdx]) % MOD
                        deepIdx += 1
                    product[outerIdx][innerIdx] = sum_val
                    innerIdx += 1
                outerIdx += 1
            return product

        def matrix_power(matrix: list[list[int]], power: int) -> list[list[int]]:
            size = 26
            ident = [[0] * size for _ in range(size)]
            idx1 = 0
            while idx1 < size:
                idx2 = 0
                while idx2 < size:
                    ident[idx1][idx2] = 1 if idx1 == idx2 else 0
                    idx2 += 1
                idx1 += 1

            pwr = power
            curBase = matrix
            continueLooping = True
            while continueLooping:
                if pwr <= 0:
                    continueLooping = False
                else:
                    if (pwr % 2) != 0:
                        ident = matrix_multiply(ident, curBase)
                    curBase = matrix_multiply(curBase, curBase)
                    pwr //= 2
            return ident

        raisedMatrix = matrix_power(deltaMatrix, t)

        freqArr = [0] * 26
        pos = 0
        while pos < len(s):
            charValue = s[pos]
            if 'A' <= charValue <= 'Z':
                idxVal = ord(charValue) - ord('A')
            else:
                idxVal = ord(charValue) - ord('a')
            freqArr[idxVal] += 1
            pos += 1

        resultFreq = [0] * 26
        i = 0
        while i < 26:
            j = 0
            while j < 26:
                resultFreq[j] = (resultFreq[j] + (freqArr[i] * raisedMatrix[i][j]) % MOD) % MOD
                j += 1
            i += 1

        finalSum = 0
        idxSum = 0
        while idxSum < 26:
            finalSum = (finalSum + resultFreq[idxSum]) % MOD
            idxSum += 1
        return finalSum