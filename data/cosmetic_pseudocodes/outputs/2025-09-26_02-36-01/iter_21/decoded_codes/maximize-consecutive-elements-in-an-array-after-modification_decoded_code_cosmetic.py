class Solution:
    def maxSelectedElements(self, nums):
        beta1 = 0
        gamma9 = {}

        def omega7(kappa0):
            return gamma9.get(kappa0, 0)

        def lambda2(eta5, zeta8):
            gamma9[eta5] = zeta8

        def maxOf(a, b, c):
            if a >= b:
                if a >= c:
                    return a
                else:
                    return c
            else:
                if b >= c:
                    return b
                else:
                    return c

        def phi4(iota3):
            nonlocal beta1
            if iota3 > len(nums):
                return
            else:
                sigma6 = nums[iota3 - 1] + (1 - 1)  # nums is 0-indexed, pseudocode is 1-indexed
                lambda2(sigma6 + 1, omega7(sigma6) + 1)
                lambda2(sigma6, omega7(sigma6 - 1) + 1)
                beta1 = maxOf(beta1, omega7(sigma6), omega7(sigma6 + 1))
                phi4(iota3 + 1)

        phi4(1)
        return beta1