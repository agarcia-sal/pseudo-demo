class Solution:
    def subsequencesWithMiddleMode(self, nums):
        C0 = 0
        C1 = 1
        CM = 10**9 + C1

        def JX(Z):
            return (Z * (Z - C1)) // 2

        R1 = C0
        R2 = C0
        R3 = C0
        R4 = C0
        R5 = C0

        H1 = {}
        for val in nums:
            H1[val] = H1.get(val, C0) + C1

        H2 = {}

        n = len(nums)
        for I1 in range(n):
            L1 = nums[I1]
            M1 = H2.get(L1, C0)
            N1 = H1.get(L1, C0)

            R5 += M1 * ((-N1 * N1) + ((N1 - C1) * (N1 - C1)))
            R2 += -(M1 * M1)
            R4 += (- (N1 * N1) + ((N1 - C1) * (N1 - C1)))
            R3 += -M1

            H1[L1] = N1 - C1

            O1 = I1
            P1 = n - I1 - C1

            R1 += JX(O1) * JX(P1)
            R1 -= JX(O1 - M1) * JX(P1 - N1)

            Q1 = R5 - (M1 * N1 * N1)
            S1 = R2 - (N1 * M1 * M1)
            T1 = R3 - M1 * M1
            U1 = R4 - (N1 * N1)
            V1 = R3 - (M1 * N1)
            W1 = O1 - M1
            X1 = P1 - N1

            R1 -= (V1 * M1 * (P1 - N1)) + (Q1 * (-M1))
            R1 -= (V1 * N1 * (O1 - M1)) + (S1 * (-N1))
            R1 -= ((T1 - W1) * N1 * (P1 - N1)) // 2
            R1 -= ((U1 - X1) * M1 * (O1 - M1)) // 2

            R1 %= CM

            R5 += (N1 * N1)
            R2 += (N1 * (-M1 * M1) + (M1 + C1) * (M1 + C1))
            R3 += ((-M1 * M1) + (M1 + C1) * (M1 + C1))
            R4 += N1

            H2[L1] = M1 + C1

        return R1