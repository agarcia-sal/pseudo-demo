from math import gcd

class Solution:
    def subsequencePairCount(self, nums):
        N = 1000000007
        M = 0
        for num in nums:
            if num > M:
                M = num

        def createMatrix(a, b):
            return [[0] * (b + 1) for _ in range(a + 1)]

        D = createMatrix(M, M)
        D[0][0] = 1

        for num in nums:
            tempDP = createMatrix(M, M)
            for X_VAR in range(M + 1):
                for Y_VAR in range(M + 1):
                    val = D[X_VAR][Y_VAR]
                    if val != 0:
                        tempDP[X_VAR][Y_VAR] = (tempDP[X_VAR][Y_VAR] + val) % N

                        newXVal = gcd(X_VAR, num)
                        tempDP[newXVal][Y_VAR] = (tempDP[newXVal][Y_VAR] + val) % N

                        newYVal = gcd(Y_VAR, num)
                        tempDP[X_VAR][newYVal] = (tempDP[X_VAR][newYVal] + val) % N
            D = tempDP

        FINAL_RESULT = 0
        for G_VAR in range(1, M + 1):
            FINAL_RESULT += D[G_VAR][G_VAR]
        FINAL_RESULT %= N
        return FINAL_RESULT