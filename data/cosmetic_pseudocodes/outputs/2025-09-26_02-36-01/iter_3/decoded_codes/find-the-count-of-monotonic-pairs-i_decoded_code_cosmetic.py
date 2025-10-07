class Solution:
    def countOfPairs(self, nums):
        remainder = 10**9 + 7
        length_nums = len(nums)
        peak = max(nums)

        # Initialize 3D dp list with zeros: dimensions length_nums x (peak+1) x (peak+1)
        dp = [[[0] * (peak + 1) for _ in range(peak + 1)] for _ in range(length_nums)]

        start_value = nums[0]
        for j in range(start_value + 1):
            k = start_value - j
            dp[0][j][k] = 1

        for i in range(1, length_nums):
            val_at_i = nums[i]
            for j2 in range(val_at_i + 1):
                k2 = val_at_i - j2
                acc = 0
                for prev_j in range(j2 + 1):
                    for prev_k in range(k2, peak + 1):
                        acc += dp[i - 1][prev_j][prev_k]
                dp[i][j2][k2] = acc % remainder

        acc = 0
        last_val = nums[-1]
        for j in range(peak + 1):
            for k in range(peak + 1):
                if j + k == last_val:
                    acc += dp[length_nums - 1][j][k]

        return acc % remainder