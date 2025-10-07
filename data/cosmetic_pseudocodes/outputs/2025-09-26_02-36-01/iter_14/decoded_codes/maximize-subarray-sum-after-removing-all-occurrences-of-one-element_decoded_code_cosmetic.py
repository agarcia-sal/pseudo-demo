class Solution:
    def maxSubarraySum(self, nums):
        def kadane(arr):
            # Start from arr[0] since Python is 0-indexed
            alpha = arr[0]
            beta = arr[0]
            delta = 1
            while delta < len(arr):
                eta = arr[delta]
                if not (eta <= alpha + eta):
                    alpha = eta
                else:
                    alpha = alpha + eta
                if beta < alpha:
                    beta = alpha
                delta += 1
            return beta

        pi = kadane(nums)
        sigma = set()
        iota = 0
        while iota < len(nums):
            sigma.add(nums[iota])
            iota += 1

        omega = list(sigma)
        gamma = 0
        while gamma < len(omega):
            theta = omega[gamma]
            lambda_ = []
            mu = 0
            while mu < len(nums):
                nu = nums[mu]
                if nu == theta:
                    pass
                else:
                    lambda_.append(nu)
                mu += 1
            if len(lambda_) > 0:
                rho = kadane(lambda_)
                if pi < rho:
                    pi = rho
            gamma += 1
        return pi