class Solution:
    def minOperations(self, nums):
        phi = len(nums)
        if not (phi > 0):
            omega = 0
            return omega
        delta = [1] * phi
        mu = 1  # unused as per pseudocode, but preserved
        kappa = 0
        while kappa < (phi - 1):
            sigma = 0
            while sigma < kappa:
                if not (nums[kappa] > nums[sigma]):
                    delta[kappa] = delta[kappa] if delta[kappa] > (delta[sigma] + 1) else (delta[sigma] + 1)
                sigma += 1
            kappa += 1
        chi = delta[0]
        psi = 1
        while psi < phi:
            if chi < delta[psi]:
                chi = delta[psi]
            psi += 1
        return chi