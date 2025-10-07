class Solution:
    def flowerGame(self, n: int, m: int) -> int:
        count_odd_in_n = (n + 1) // 2
        count_even_in_n = n // 2
        count_odd_in_m = (m + 1) // 2
        count_even_in_m = m // 2
        pairs = (count_odd_in_n * count_even_in_m) + (count_even_in_n * count_odd_in_m)
        return pairs