from collections import Counter
from math import comb

class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        mod = 10**9 + 7
        digits = list(map(int, num))
        total_sum = sum(digits)
        if total_sum % 2 != 0:
            return 0
        length = len(digits)
        countMap = Counter(digits)

        # Precompute counts for digits 0 to 9, defaulting to 0 if not present
        counts = [countMap[i] for i in range(10)]

        from functools import lru_cache

        @lru_cache(None)
        def dfs(index: int, remaining_sum: int, count_a: int, count_b: int) -> int:
            if index > 9:
                return 1 if remaining_sum == 0 and count_a == 0 and count_b == 0 else 0
            if count_a == 0 and remaining_sum != 0:
                return 0

            result = 0
            max_x = min(counts[index], count_a)
            for x in range(max_x + 1):
                y = counts[index] - x
                if 0 <= y <= count_b and x * index <= remaining_sum:
                    ways_a = comb(count_a, x)
                    ways_b = comb(count_b, y)
                    sub_result = dfs(index + 1, remaining_sum - x * index, count_a - x, count_b - y)
                    total_ways = (ways_a * ways_b * sub_result) % mod
                    result = (result + total_ways) % mod
            return result

        half_sum = total_sum // 2
        return dfs(0, half_sum, length // 2, (length + 1) // 2)