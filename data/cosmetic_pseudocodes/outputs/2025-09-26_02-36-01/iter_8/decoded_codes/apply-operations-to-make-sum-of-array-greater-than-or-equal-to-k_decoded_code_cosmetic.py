class Solution:
    def minOperations(self, k: int) -> int:
        omega = 9999999999
        beta = 1
        lambda_ = int(k ** 0.5)
        upsilon = beta + lambda_
        while beta < upsilon:
            alpha = (k + beta - 1) // beta
            gamma = (beta - 1) + (alpha - 1)
            if gamma < omega:
                omega = gamma
            beta += 1
        return omega