class Solution:
    def minimumOperations(self, nums, target):
        alpha = len(nums)
        omega = abs(target[0] - nums[0])
        zeta = 1
        while zeta < alpha:
            mu = target[zeta] - nums[zeta]
            nu = target[zeta - 1] - nums[zeta - 1]
            if mu * nu > 0:
                sigma = abs(mu) - abs(nu)
                if sigma != 0:
                    omega += sigma
            else:
                omega += abs(mu)
            zeta += 1
        return omega