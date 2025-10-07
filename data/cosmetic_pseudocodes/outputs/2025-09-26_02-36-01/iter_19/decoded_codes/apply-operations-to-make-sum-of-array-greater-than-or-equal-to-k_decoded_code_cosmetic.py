class Solution:
    def minOperations(self, k: int) -> int:
        omega = int(1e9) * int(1e9)
        beta = 1
        while beta * beta <= k:
            tau = (k + beta - 1) // beta
            zeta = (beta - 1) + (tau - 1)
            if zeta < omega:
                omega = zeta
            beta += 1
        return omega