class Solution:
    def maxSubarraySum(self, nums):
        def kadane(arr):
            if not arr:
                return 0
            alpha = beta = arr[0]
            gamma = 1
            while gamma < len(arr):
                delta = arr[gamma]
                if delta > alpha + delta:
                    alpha = delta
                else:
                    alpha = alpha + delta
                if beta < alpha:
                    beta = alpha
                gamma += 1
            return beta

        omega = kadane(nums)
        epsilon = set()
        zeta = 0
        while zeta < len(nums):
            epsilon.add(nums[zeta])
            zeta += 1

        theta = next(iter(epsilon), None)
        iota = 0
        while iota < len(epsilon):
            rho = []

            kappa = 0
            epsilon_list = list(epsilon)
            while kappa < len(nums):
                psi = nums[kappa]
                if psi != epsilon_list[iota]:
                    rho.append(psi)
                kappa += 1

            if len(rho) > 0:
                sigma = kadane(rho)
                if omega < sigma:
                    omega = sigma

            iota += 1

        return omega