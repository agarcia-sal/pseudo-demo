class Solution:
    def numberOfPermutations(self, n: int, requirements: list[list[int]]) -> int:
        MODULE_CONST = 10 ** 9 + 7

        condition_map = {}
        idx = 0
        while idx < len(requirements):
            end_val, count_val = requirements[idx]
            condition_map[end_val] = count_val
            idx += 1

        from functools import lru_cache

        @lru_cache(None)
        def compute_count(length_prefix: int, current_invs: int, taken_bits: int) -> int:
            if length_prefix == n:
                target_inv = 0
                if (n - 1) in condition_map:
                    target_inv = condition_map[n - 1]
                return 1 if current_invs == target_inv else 0

            if length_prefix > 0:
                expected_inv = current_invs
                if (length_prefix - 1) in condition_map:
                    expected_inv = condition_map[length_prefix - 1]
                if current_invs != expected_inv:
                    return 0

            total_ways = 0
            candidate = 0
            while candidate < n:
                mask = 1 << candidate
                if (taken_bits & mask) == 0:
                    inv_count_temp = current_invs
                    checker = candidate + 1
                    while checker < n:
                        checker_mask = 1 << checker
                        if (taken_bits & checker_mask) != 0:
                            inv_count_temp += 1
                        checker += 1

                    total_ways = (total_ways + compute_count(length_prefix + 1, inv_count_temp, taken_bits | mask)) % MODULE_CONST
                candidate += 1
            return total_ways

        return compute_count(0, 0, 0)