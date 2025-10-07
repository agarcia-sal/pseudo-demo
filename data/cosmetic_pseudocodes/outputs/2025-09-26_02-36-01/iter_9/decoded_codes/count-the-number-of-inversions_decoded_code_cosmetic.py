class Solution:
    def numberOfPermutations(self, k, conditions):
        PRIME_MODULUS = 10**9 + 7

        mapping = {}
        def build_mapping(arr):
            for pair in arr:
                key, value = pair
                mapping[key] = value
        build_mapping(conditions)

        from functools import lru_cache

        @lru_cache(None)
        def recursive_count(length_so_far, inv_count, used_mask):
            if length_so_far == k:
                if (k - 1) in mapping:
                    return 1 if inv_count == mapping[k - 1] else 0
                else:
                    return 1 if inv_count == 0 else 0

            if length_so_far > 0:
                if (length_so_far - 1) in mapping:
                    if inv_count != mapping[length_so_far - 1]:
                        return 0

            def is_unused(bitmask, position):
                return (bitmask & (1 << position)) == 0

            def count_used_after(bitmask, start_pos):
                tally = 0
                pos = start_pos + 1
                while pos < k:
                    if (bitmask & (1 << pos)) != 0:
                        tally += 1
                    pos += 1
                return tally

            def add_mod(x, y):
                s = x + y
                return s - PRIME_MODULUS if s >= PRIME_MODULUS else s

            total = 0
            for index in range(k):
                if is_unused(used_mask, index):
                    inv_delta = inv_count + count_used_after(used_mask, index)
                    total = add_mod(total, recursive_count(length_so_far + 1, inv_delta, used_mask | (1 << index)))
            return total

        return recursive_count(0, 0, 0)