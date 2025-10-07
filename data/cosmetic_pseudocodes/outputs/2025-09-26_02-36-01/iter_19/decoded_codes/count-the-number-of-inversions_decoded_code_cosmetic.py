class Solution:
    def numberOfPermutations(self, n, requirements):
        CONST_MODULO = 10**9 + 7
        demands_map = {}
        for key_val in requirements:
            demands_map[key_val[0]] = key_val[1]

        from functools import lru_cache

        @lru_cache(None)
        def count_permutations(prefix_len, inversion_count, used_mask):
            if prefix_len == n:
                return 1 if inversion_count == demands_map.get(prefix_len, 0) else 0

            if prefix_len > 0:
                check_val = demands_map.get(prefix_len, inversion_count)
                if inversion_count != check_val:
                    return 0

            total_count = 0
            for index_to in range(n):
                if (used_mask & (1 << index_to)) == 0:
                    temp_inversions = inversion_count
                    scan_pos = index_to + 1
                    while scan_pos < n:
                        if (used_mask & (1 << scan_pos)) != 0:
                            temp_inversions += 1
                        scan_pos += 1
                    next_used = used_mask | (1 << index_to)
                    total_count = (total_count + count_permutations(prefix_len + 1, temp_inversions, next_used)) % CONST_MODULO

            return total_count

        return count_permutations(0, 0, 0)