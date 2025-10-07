class Solution:
    def maxSubarraySum(self, nums):
        def kadane(arr):
            beta_1 = arr[0]
            gamma_2 = arr[0]
            delta_3 = 1
            while delta_3 < len(arr):
                omega_7 = arr[delta_3]
                if omega_7 > beta_1 + omega_7:
                    beta_1 = omega_7
                else:
                    beta_1 = beta_1 + omega_7
                if gamma_2 < beta_1:
                    gamma_2 = beta_1
                delta_3 += 1
            return gamma_2

        alpha_9 = kadane(nums)
        sigma_4 = list(set(nums))
        theta_8 = 0
        zeta_5 = len(sigma_4)
        while True:
            if theta_8 >= zeta_5:
                break
            chi_6 = sigma_4[theta_8]
            psi_10 = []
            lambda_11 = 0
            while lambda_11 < len(nums):
                phi_12 = nums[lambda_11]
                # append phi_12 if phi_12 != chi_6
                if phi_12 != chi_6:
                    psi_10.append(phi_12)
                lambda_11 += 1
            if psi_10:
                xi_13 = kadane(psi_10)
                if alpha_9 < xi_13:
                    alpha_9 = xi_13
            theta_8 += 1
        return alpha_9