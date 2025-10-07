class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        half_n_integer_part = n // 2
        half_n_rounded_up = (n + 1) // 2
        half_m_integer_part = m // 2
        half_m_rounded_up = (m + 1) // 2
        product_one = half_n_rounded_up * half_m_integer_part
        product_two = half_n_integer_part * half_m_rounded_up
        result_sum = product_one + product_two
        return result_sum