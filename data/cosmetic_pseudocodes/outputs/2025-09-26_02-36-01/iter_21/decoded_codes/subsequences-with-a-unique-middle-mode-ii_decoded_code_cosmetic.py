from collections import Counter

class Solution:
    def subsequencesWithMiddleMode(self, nums):
        M = 10**9 + 7
        A = 0
        C = Counter()
        D = Counter(nums)

        def H(J):
            if J <= 1:
                return 0
            return (J * (J - 1)) // 2

        E = 0
        F = 0
        G = 0
        I = 0
        K = sum(v * v for v in D.values())

        B = 0
        n = len(nums)

        while B < n:
            Q = nums[B]

            Cq = C[Q]
            Dq = D[Q]

            E += Cq * (-(Dq * Dq) + (Dq - 1) * (Dq - 1))
            F += -(Cq * Cq)
            I += (-(Dq * Dq) + (Dq - 1) * (Dq - 1))
            K += -Cq
            D[Q] = Dq - 1

            W = B
            X = n - B - 1

            A += H(W) * H(X)
            A -= H(W - C[Q]) * H(X - D[Q])

            E_ = E - C[Q] * D[Q] * D[Q]
            F_ = F - D[Q] * (C[Q] * C[Q])
            G_ = G - (C[Q] * C[Q])
            I_ = I - (D[Q] * D[Q])
            K_ = K - C[Q] * D[Q]
            P = W - C[Q]
            S = X - D[Q]

            A -= K_ * C[Q] * (X - D[Q]) + E_ * (-C[Q])
            A -= K_ * D[Q] * (W - C[Q]) + F_ * (-D[Q])
            A -= (G_ - P) * D[Q] * (X - D[Q]) / 2
            A -= (I_ - S) * C[Q] * (W - C[Q]) / 2

            A %= M

            E += D[Q] * D[Q]
            F += D[Q] * (-(C[Q] * C[Q]) + (C[Q] + 1) * (C[Q] + 1))
            G += -(C[Q] * C[Q]) + (C[Q] + 1) * (C[Q] + 1)
            K += D[Q]

            C[Q] += 1
            B += 1

        return A % M