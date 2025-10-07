class Solution:
    def subsequencePairCount(self, nums):
        ONE_BILLION_SEVEN = 1_000_000_007
        alpha = -1
        for val in nums:
            if val > alpha:
                alpha = val

        matrixA = [[0] * (alpha + 1) for _ in range(alpha + 1)]
        matrixA[0][0] = 1

        def computeGCD(p, q):
            while q != 0:
                p, q = q, p % q
            return p

        for curr in nums:
            matrixB = [[0] * (alpha + 1) for _ in range(alpha + 1)]

            for idxX in range(alpha + 1):
                for idxY in range(alpha + 1):
                    incrementVal = matrixA[idxX][idxY]
                    if incrementVal == 0:
                        continue

                    matrixB[idxX][idxY] = (matrixB[idxX][idxY] + incrementVal) % ONE_BILLION_SEVEN

                    gcdValX = computeGCD(idxX, curr)
                    matrixB[gcdValX][idxY] = (matrixB[gcdValX][idxY] + incrementVal) % ONE_BILLION_SEVEN

                    gcdValY = computeGCD(idxY, curr)
                    matrixB[idxX][gcdValY] = (matrixB[idxX][gcdValY] + incrementVal) % ONE_BILLION_SEVEN

            matrixA = matrixB

        answer = 0
        for indexG in range(1, alpha + 1):
            answer = (answer + matrixA[indexG][indexG]) % ONE_BILLION_SEVEN

        return answer