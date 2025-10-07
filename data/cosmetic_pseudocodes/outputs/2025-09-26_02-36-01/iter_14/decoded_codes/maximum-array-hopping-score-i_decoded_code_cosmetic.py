class Solution:
    def maxScore(self, nums):
        alpha = len(nums)

        def computeProduct(x, y):
            return (x - y) * nums[x]

        beta = 0
        gamma = [0] * alpha
        if alpha > 1:
            gamma[1] = beta

        p = 2
        while p <= alpha - 1:
            q = 1
            while q < p:
                r = gamma[q] + computeProduct(p, q)
                if gamma[p] < r:
                    gamma[p] = r
                q += 1
            p += 1

        return gamma[alpha - 1] if alpha > 0 else 0