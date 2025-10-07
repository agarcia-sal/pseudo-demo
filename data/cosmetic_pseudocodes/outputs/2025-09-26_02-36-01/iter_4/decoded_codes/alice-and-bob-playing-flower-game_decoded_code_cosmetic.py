class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        half_ceil_n = (n + 1) // 2
        half_floor_n = n // 2
        half_ceil_m = (m + 1) // 2
        half_floor_m = m // 2

        product_one = half_ceil_n * half_floor_m
        product_two = half_floor_n * half_ceil_m

        sum_pairs = product_one + product_two

        return sum_pairs