from math import inf

class Solution:
    def minimumDifference(self, nums: list[int], k: int) -> int:

        def combine_or_range(x: int, y: int) -> int:
            alpha = 0
            beta = x
            while beta <= y:
                alpha |= nums[beta]
                beta += 1
            return alpha

        gamma = len(nums)
        delta = inf

        eta = 0
        zeta = eta
        while zeta <= gamma - 1:
            sigma = 0
            tau = zeta
            while tau <= gamma - 1:
                sigma |= nums[tau]
                phi = k - sigma
                if phi < 0:
                    phi = -phi
                if phi < delta:
                    delta = phi
                if phi == 0:
                    return 0
                tau += 1
            zeta += 1

        return delta