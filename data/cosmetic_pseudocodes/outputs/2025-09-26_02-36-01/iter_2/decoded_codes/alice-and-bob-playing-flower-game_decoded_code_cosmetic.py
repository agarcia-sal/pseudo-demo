class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        half_ceil_n = (n + 1) // 2
        half_floor_n = n // 2
        half_ceil_m = (m + 1) // 2
        half_floor_m = m // 2
        mixed_pairs1 = half_ceil_n * half_floor_m
        mixed_pairs2 = half_floor_n * half_ceil_m
        combined_pairs = mixed_pairs1 + mixed_pairs2
        return combined_pairs