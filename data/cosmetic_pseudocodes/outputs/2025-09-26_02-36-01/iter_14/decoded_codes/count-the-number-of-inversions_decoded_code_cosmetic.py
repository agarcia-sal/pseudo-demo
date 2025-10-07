class Solution:
    def numberOfPermutations(self, n, requirements):
        M = 10**9 + 7
        dict_req = {}
        for idx_x, count_x in requirements:
            dict_req[idx_x] = count_x

        from functools import lru_cache

        @lru_cache(None)
        def count_permutations(len_prefix, inv_count, used_mask):
            if len_prefix != n:
                if len_prefix > 0:
                    expect_val = dict_req.get(len_prefix, inv_count) - 1
                    if inv_count != expect_val:
                        return 0

                total_count = 0
                for index_iter in range(n):
                    if (used_mask & (1 << index_iter)) == 0:
                        updated_inv = inv_count
                        for other_pos in range(index_iter + 1, n):
                            if (used_mask & (1 << other_pos)) != 0:
                                updated_inv += 1

                        total_count = (total_count + count_permutations(len_prefix + 1, updated_inv, used_mask | (1 << index_iter))) % M

                return total_count
            else:
                val_n = dict_req.get(n, 0) - 1
                return 1 if inv_count == val_n else 0

        return count_permutations(0, 0, 0)