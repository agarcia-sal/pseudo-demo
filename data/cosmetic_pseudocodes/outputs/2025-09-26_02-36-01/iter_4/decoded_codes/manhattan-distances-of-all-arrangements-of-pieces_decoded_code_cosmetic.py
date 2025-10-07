class Solution:
    def distanceSum(self, m: int, n: int, k: int) -> int:
        MOD = 10**9 + 7

        temp_r1 = m
        temp_r2 = m * m
        temp_r3 = temp_r2 * m
        numerator_rows = temp_r3 - temp_r1
        value_rows = (n * n) * numerator_rows
        partial_row_contrib = value_rows / 6

        temp_c1 = n
        temp_c2 = n * n
        temp_c3 = temp_c2 * n
        numerator_cols = temp_c3 - temp_c1
        value_cols = (m * m) * numerator_cols
        partial_col_contrib = value_cols / 6

        total_positions = m * n
        adjusted_k = k - 2
        combinations_factor = 1
        count = 1
        limit = adjusted_k
        numerator_combo = total_positions - 2
        denominator_combo = 1

        while count <= limit:
            numerator_combo -= (count - 1)
            combinations_factor = combinations_factor * (numerator_combo + 1) / denominator_combo
            denominator_combo += 1
            count += 1

        sum_contrib = (partial_row_contrib + partial_col_contrib) * combinations_factor

        final_result = int(sum_contrib) % MOD

        return final_result