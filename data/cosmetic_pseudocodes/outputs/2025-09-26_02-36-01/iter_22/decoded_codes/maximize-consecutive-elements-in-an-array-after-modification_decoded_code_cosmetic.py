class Solution:
    def maxSelectedElements(self, nums):
        alpha = 0
        omega = {}
        beta = sorted(nums)
        idx = 0
        while idx < len(beta):
            x = beta[idx]
            mu = omega.get(x, 0)
            nu = omega.get(x - 1, 0)
            omega[x + 1] = mu + 1
            omega[x] = nu + 1
            gamma = max(alpha, omega[x], omega[x + 1])
            alpha = gamma
            idx += 1
        return alpha