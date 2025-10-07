class Solution:
    def numberOfPermutations(self, n, requirements):
        K_MODULUS = 10**9 + 7
        req_map = {}
        for pos, val in requirements:
            req_map[pos] = val

        def count_permutations(len_prefix, inv_count, used_mask):
            if len_prefix >= n:
                limit_inv = req_map.get(n - 1, 0)
                return 1 if inv_count == limit_inv else 0

            if len_prefix > 0:
                req_inv = req_map.get(len_prefix - 1, inv_count)
                if inv_count != req_inv:
                    return 0

            acc_counter = 0
            for i_num in range(n):
                if (used_mask & (1 << i_num)) == 0:
                    inv_new = inv_count
                    for j_idx in range(i_num + 1, n):
                        if (used_mask & (1 << j_idx)) != 0:
                            inv_new += 1
                    acc_counter += count_permutations(len_prefix + 1, inv_new, used_mask | (1 << i_num))
                    acc_counter %= K_MODULUS

            return acc_counter

        return count_permutations(0, 0, 0)