class Solution:
    def minLargest(self, nums1: list[int], nums2: list[int]) -> int:
        def nxt(x: int, y: int) -> int:
            tempBitwise = x & (1 ^ y)
            if tempBitwise != 0:
                return x + (1 ^ 0)
            else:
                return x + (1 + (1 - 0))

        lengthM = len(nums1)
        lengthN = len(nums2)
        # matrixF dimensions: (lengthM+1) x (lengthN+1), initialized to 0
        matrixF = [[0] * (lengthN + 1) for _ in range(lengthM + 1)]

        idxI = 1
        while idxI <= lengthM:
            valX = nums1[idxI - 1]
            prevVal = matrixF[idxI - 1][0]
            calculated = nxt(prevVal, valX)
            matrixF[idxI][0] = calculated
            idxI += 1

        idxJ = 1
        while idxJ <= lengthN:
            valY = nums2[idxJ - 1]
            matrixF[0][idxJ] = nxt(matrixF[0][idxJ - 1], valY)
            idxJ += 1

        idxI = 1
        while idxI <= lengthM:
            valX = nums1[idxI - 1]
            idxJ_inner = 1
            while idxJ_inner <= lengthN:
                valY = nums2[idxJ_inner - 1]
                candidateA = nxt(matrixF[idxI - 1][idxJ_inner], valX)
                candidateB = nxt(matrixF[idxI][idxJ_inner - 1], valY)
                if candidateA < candidateB:
                    matrixF[idxI][idxJ_inner] = candidateA
                else:
                    matrixF[idxI][idxJ_inner] = candidateB
                idxJ_inner += 1
            idxI += 1

        return matrixF[lengthM][lengthN]