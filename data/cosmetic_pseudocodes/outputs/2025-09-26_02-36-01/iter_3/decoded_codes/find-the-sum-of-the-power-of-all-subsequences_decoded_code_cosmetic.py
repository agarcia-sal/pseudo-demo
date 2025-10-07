class Solution:
    def sumOfPower(self, nums, k):
        modulus = 10**9 + 7
        length = len(nums)
        dp = [[0] * (k + 1) for _ in range(length + 1)]
        dp[0][0] = 1

        for idx_outer in range(1, length + 1):
            for idx_inner in range(k + 1):
                dp[idx_outer][idx_inner] = dp[idx_outer - 1][idx_inner]
                if idx_inner >= nums[idx_outer - 1]:
                    dp[idx_outer][idx_inner] += dp[idx_outer - 1][idx_inner - nums[idx_outer - 1]]
                dp[idx_outer][idx_inner] %= modulus

        aggregate_power = 0
        upper_limit = (1 << length) - 1
        for subset_id in range(1, upper_limit + 1):
            partial_sum = 0
            elems_count = 0
            bit_pos = 0
            while bit_pos < length:
                if subset_id & (1 << bit_pos):
                    partial_sum += nums[bit_pos]
                    elems_count += 1
                bit_pos += 1
            if partial_sum == k:
                aggregate_power += pow(2, length - elems_count, modulus)
                aggregate_power %= modulus

        return aggregate_power