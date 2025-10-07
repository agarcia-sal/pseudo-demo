from math import gcd
from typing import List

class Solution:
    def subsequencePairCount(self, numbers: List[int]) -> int:
        MODULUS = 10**9 + 7
        highest = numbers[0]
        index = 1
        while index < len(numbers):
            if numbers[index] > highest:
                highest = numbers[index]
            index += 1

        row_count = highest + 1
        col_count = highest + 1
        dp_table = [[0] * col_count for _ in range(row_count)]

        dp_table[0][0] = 1

        i = 0
        while i < len(numbers):
            current_number = numbers[i]
            updated_dp = [[0] * col_count for _ in range(row_count)]

            x = 0
            while x < row_count:
                y = 0
                while y < col_count:
                    curr_val = dp_table[x][y]

                    val1 = updated_dp[x][y] + curr_val
                    val1_mod = val1 % MODULUS
                    updated_dp[x][y] = val1_mod

                    gcd_x = gcd(x, current_number)
                    val2 = updated_dp[gcd_x][y] + curr_val
                    val2_mod = val2 % MODULUS
                    updated_dp[gcd_x][y] = val2_mod

                    gcd_y = gcd(y, current_number)
                    val3 = updated_dp[x][gcd_y] + curr_val
                    updated_dp[x][gcd_y] = val3 % MODULUS

                    y += 1
                x += 1

            dp_table = updated_dp
            i += 1

        total = 0
        g = 1
        while g <= highest:
            total += dp_table[g][g]
            g += 1

        answer = total % MODULUS
        return answer