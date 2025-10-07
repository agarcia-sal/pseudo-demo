class Solution:
    def subsequencePairCount(self, A):
        K = 10**9 + 7

        def gcdHelper(p, q):
            while q != 0:
                p, q = q, p % q
            return p

        def zeroMatrix(rows, cols):
            return [[0] * cols for _ in range(rows)]

        maxVal = A[0]
        idx1 = 1
        while idx1 < len(A):
            if A[idx1] > maxVal:
                maxVal = A[idx1]
            idx1 += 1

        dpMatrix = zeroMatrix(maxVal + 1, maxVal + 1)
        dpMatrix[0][0] = 1

        def copyAndUpdateDP(arrOld, val):
            newMatrix = zeroMatrix(maxVal + 1, maxVal + 1)
            rCtr = 0
            while rCtr <= maxVal:
                cCtr = 0
                while cCtr <= maxVal:
                    baseCount = arrOld[rCtr][cCtr]
                    if baseCount != 0:
                        newMatrix[rCtr][cCtr] = (newMatrix[rCtr][cCtr] + baseCount) % K

                        gcdX = gcdHelper(rCtr, val)
                        newMatrix[gcdX][cCtr] = (newMatrix[gcdX][cCtr] + baseCount) % K

                        gcdY = gcdHelper(cCtr, val)
                        newMatrix[rCtr][gcdY] = (newMatrix[rCtr][gcdY] + baseCount) % K
                    cCtr += 1
                rCtr += 1
            return newMatrix

        pos = 0
        while pos < len(A):
            dpMatrix = copyAndUpdateDP(dpMatrix, A[pos])
            pos += 1

        finalAccum = 0
        idx2 = 1
        while idx2 <= maxVal:
            finalAccum += dpMatrix[idx2][idx2]
            idx2 += 1

        return finalAccum % K