class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        alpha = 0
        beta = float('-inf')
        gamma = {}

        delta = 0
        epsilon = len(nums)

        while delta != epsilon:
            zeta = nums[delta]

            if (zeta - k) in gamma:
                eta = gamma[zeta - k]
                theta = (alpha - eta) + zeta
                if theta > beta:
                    beta = theta

            if (zeta + k) in gamma:
                iota = gamma[zeta + k]
                kappa = (alpha - iota) + zeta
                if kappa > beta:
                    beta = kappa

            if zeta in gamma:
                lambd = gamma[zeta]
                if alpha < lambd:
                    gamma[zeta] = alpha
            else:
                gamma[zeta] = alpha

            alpha += zeta
            delta += 1

        return beta if beta != float('-inf') else 0