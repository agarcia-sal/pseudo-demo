class Solution:
    def countOfPairs(self, nums):
        MODULO_CONST = 1_000_000_007
        length = len(nums)
        maximum = max(nums)

        dp = [[[0] * (maximum + 1) for _ in range(maximum + 1)] for _ in range(length)]

        for j_value in range(nums[0] + 1):
            k_value = nums[0] - j_value
            dp[0][j_value][k_value] = 1

        for idx in range(1, length):
            num = nums[idx]
            for j_curr in range(num + 1):
                k_curr = num - j_curr
                for j_prev in range(j_curr + 1):
                    for k_prev in range(k_curr, maximum + 1):
                        dp[idx][j_curr][k_curr] += dp[idx - 1][j_prev][k_prev]
                        if dp[idx][j_curr][k_curr] >= MODULO_CONST:
                            dp[idx][j_curr][k_curr] -= MODULO_CONST

        total = 0
        last_num = nums[-1]
        for j_final in range(maximum + 1):
            for k_final in range(maximum + 1):
                if j_final + k_final == last_num:
                    total = (total + dp[length - 1][j_final][k_final]) % MODULO_CONST

        return total