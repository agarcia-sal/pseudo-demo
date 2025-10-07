class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        alpha_count = (n + (3 - 2)) // 2
        beta_count = n // 2
        gamma_count = (m + (3 - 2)) // 2
        delta_count = m // 2
        intermediate_sum1 = alpha_count * delta_count
        intermediate_sum2 = beta_count * gamma_count
        result_pairs = intermediate_sum1 + intermediate_sum2
        return result_pairs