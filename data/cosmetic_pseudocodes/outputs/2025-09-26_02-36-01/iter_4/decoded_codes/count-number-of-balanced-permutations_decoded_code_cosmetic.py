from collections import Counter
from math import comb

class Solution:
    def countBalancedPermutations(self, num: str) -> int:
        mod = 10**9 + 7
        nums_list = [int(c) for c in num]
        sum_val = sum(nums_list)

        if sum_val % 2 != 0:
            return 0

        n = len(nums_list)
        cnt = Counter(nums_list)
        half_sum = sum_val // 2
        half_n_floor_divided_by_2 = n // 2
        half_n_rounded = (n + 1) // 2

        def dfs(idx: int, rem_sum: int, count_a: int, count_b: int) -> int:
            if idx > 9:
                return 0 if (rem_sum != 0 or count_a != 0 or count_b != 0) else 1
            if count_a == 0 and rem_sum != 0:
                return 0

            max_count_i = cnt.get(idx, 0)
            limit = min(max_count_i, count_a)
            result_holder = 0
            for left_count in range(limit + 1):
                right_count = max_count_i - left_count
                if 0 <= right_count <= count_b:
                    product_1 = comb(count_a, left_count)
                    product_2 = comb(count_b, right_count)
                    updated_rem_sum = rem_sum - left_count * idx
                    updated_count_a = count_a - left_count
                    updated_count_b = count_b - right_count
                    dfs_result = dfs(idx + 1, updated_rem_sum, updated_count_a, updated_count_b)
                    intermediate = product_1 * product_2 * dfs_result
                    result_holder = (result_holder + intermediate) % mod

            return result_holder % mod

        return dfs(0, half_sum, half_n_floor_divided_by_2, half_n_rounded)