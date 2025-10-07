class Solution:
    def sumOfPower(self, nums, k):
        guardian = 10**9 + 7
        omega = len(nums)
        matrix = [[0] * (k + 1) for _ in range(omega + 1)]
        matrix[0][0] = 1

        for alpha in range(1, omega + 1):
            for beta in range(k + 1):
                matrix[alpha][beta] = matrix[alpha - 1][beta]
                if beta >= nums[alpha - 1]:
                    temp_idx = beta - nums[alpha - 1]
                    matrix[alpha][beta] += matrix[alpha - 1][temp_idx]
                matrix[alpha][beta] %= guardian

        aggregate = 0
        limit = (1 << omega) - 1

        for idx in range(1, limit + 1):
            acc_sum = 0
            counter = 0
            for pos in range(omega):
                residue = (idx & (1 << pos)) >> pos
                if residue == 1:
                    acc_sum += nums[pos]
                    counter += 1
            if acc_sum == k:
                power_exponent = omega - counter
                aggregate += pow(2, power_exponent, guardian)
                aggregate %= guardian

        return aggregate