class Solution:
    def countOfPairs(self, nums):
        THRESHOLD = 10**9 + 7  # 10^9 + 7

        alpha = len(nums)
        beta = float('-inf')
        gamma = 0

        while gamma < alpha:
            if nums[gamma] > beta:
                beta = nums[gamma]
            gamma += 1

        matrix = []
        lambda_ = 0
        while lambda_ < alpha + 1:
            second_dim = []
            mu = 0
            while mu < beta + 1:
                third_dim = []
                nu = 0
                while nu < beta + 1:
                    third_dim.append(0)
                    nu += 1
                second_dim.append(third_dim)
                mu += 1
            matrix.append(second_dim)
            lambda_ += 1

        phi = 0
        while phi <= nums[0]:
            matrix[1][phi][nums[0] - phi] = 1
            phi += 1

        xi = 2
        while xi <= alpha:
            sigma = 0
            while sigma <= nums[xi - 1]:
                tau = 0
                while tau <= nums[xi - 1]:
                    if sigma + tau == nums[xi - 1]:
                        rho = 0
                        while rho <= sigma:
                            psi = tau
                            while psi <= beta:
                                matrix[xi][sigma][tau] += matrix[xi - 1][rho][psi]
                                matrix[xi][sigma][tau] %= THRESHOLD
                                psi += 1
                            rho += 1
                    tau += 1
                sigma += 1
            xi += 1

        zeta = 0
        omega = 0
        tau_result = 0

        while zeta <= beta:
            omega = 0
            while omega <= beta:
                tau_result += matrix[alpha][zeta][omega]
                tau_result %= THRESHOLD
                omega += 1
            zeta += 1

        return tau_result