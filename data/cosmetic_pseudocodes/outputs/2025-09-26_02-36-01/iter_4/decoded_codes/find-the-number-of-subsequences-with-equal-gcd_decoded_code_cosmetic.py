from math import gcd

class Solution:
    def subsequencePairCount(self, nums):
        MODULO = 10**9 + 7
        max_value = max(nums) if nums else 0
        dp_table = [[0] * (max_value + 1) for _ in range(max_value + 1)]
        dp_table[0][0] = 1

        for current_num in nums:
            temp_dp = [[0] * (max_value + 1) for _ in range(max_value + 1)]
            for i in range(max_value + 1):
                for j in range(max_value + 1):
                    val = dp_table[i][j]
                    if val == 0:
                        continue
                    temp_dp[i][j] = (temp_dp[i][j] + val) % MODULO

                    gcd_x_num = gcd(i, current_num)
                    temp_dp[gcd_x_num][j] = (temp_dp[gcd_x_num][j] + val) % MODULO

                    gcd_y_num = gcd(j, current_num)
                    temp_dp[i][gcd_y_num] = (temp_dp[i][gcd_y_num] + val) % MODULO
            dp_table = temp_dp

        total = 0
        for g_counter in range(1, max_value + 1):
            total = (total + dp_table[g_counter][g_counter]) % MODULO
        return total