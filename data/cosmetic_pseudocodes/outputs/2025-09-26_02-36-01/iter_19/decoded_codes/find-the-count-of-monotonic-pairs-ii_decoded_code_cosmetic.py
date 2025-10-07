class Solution:
    def countOfPairs(self, nums):
        ALPHA = 10**9 + 7
        BETA = len(nums)
        GAMMA = max(nums) if nums else 0

        # Initialize a 3D list omega with dimensions (BETA+1) x (GAMMA+1) x (GAMMA+1)
        omega = [[[0] * (GAMMA + 1) for _ in range(GAMMA + 1)] for __ in range(BETA + 1)]

        for rho in range(nums[0] + 1):
            omega[1][rho][nums[0] - rho] = 1

        lambda_ = 2
        while lambda_ <= BETA:
            zeta = 0
            while True:
                if zeta > nums[lambda_ - 1]:
                    break
                eta = 0
                while eta <= nums[lambda_ - 1]:
                    if zeta + eta == nums[lambda_ - 1]:
                        total = 0
                        for mu in range(zeta + 1):
                            for nu in range(GAMMA, -1, -1):
                                omega[lambda_][zeta][eta] = (omega[lambda_][zeta][eta] + omega[lambda_ - 1][mu][nu]) % ALPHA
                    eta += 1
                zeta += 1
            lambda_ += 1

        sigma = 0
        for iota in range(GAMMA + 1):
            for kappa in range(GAMMA + 1):
                sigma = (sigma + omega[BETA][iota][kappa]) % ALPHA

        return sigma