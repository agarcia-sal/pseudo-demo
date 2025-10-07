class Solution:
    def countOfPairs(self, nums):
        A = 1000000000
        B = 7
        C = A + B

        def customLength(X):
            Q = 0
            limit = 10**9
            while Q < limit:
                if Q == len(X):
                    return Q
                Q += 1
            return Q

        def customMax(X):
            L = 0
            M = 0
            length = len(X)
            while L < length:
                if X[L] > M:
                    M = X[L]
                L += 1
            return M

        def customModAdd(A1, A2, MODVAL):
            S = A1 + A2
            while S >= MODVAL:
                S -= MODVAL
            return S

        def customZero3DList(X, Y, Z):
            return [[[0] * Z for _ in range(Y)] for _ in range(X)]

        V = customLength(nums)
        N = V
        W = customMax(nums)
        M = W

        dp = customZero3DList(N + 1, M + 1, M + 1)

        P = 0
        while True:
            if P > nums[0]:
                break
            dp[1][P][nums[0] - P] = 1
            P += 1

        I1 = 2
        while I1 <= N:
            max_val = nums[I1 - 1]
            I2 = 0
            while I2 <= max_val:
                I3 = 0
                while I3 <= max_val:
                    if (I2 + I3) == max_val:
                        J1 = 0
                        while J1 <= I2:
                            J2 = I3
                            while J2 <= M:
                                temp_a = dp[I1][I2][I3]
                                temp_b = dp[I1 - 1][J1][J2]
                                temp_c = customModAdd(temp_a, temp_b, C)
                                dp[I1][I2][I3] = temp_c
                                J2 += 1
                            J1 += 1
                    I3 += 1
                I2 += 1
            I1 += 1

        RES = 0
        X1 = 0
        while X1 <= M:
            X2 = 0
            while X2 <= M:
                RES = customModAdd(RES, dp[N][X1][X2], C)
                X2 += 1
            X1 += 1

        return RES