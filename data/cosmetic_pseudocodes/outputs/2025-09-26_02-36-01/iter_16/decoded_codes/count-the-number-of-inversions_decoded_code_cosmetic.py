class Solution:
    def numberOfPermutations(self, n: int, requirements: list[list[int]]) -> int:
        CONST_MOD = 10**9 + 7
        map_reqs = {key_pos: val_count for key_pos, val_count in requirements}

        def count_permutations(len_pre: int, count_inv: int, bits_used: int) -> int:
            if len_pre == n:
                req_inv = map_reqs.get(n - 1, 0)
                return 1 if count_inv == req_inv else 0

            if len_pre > 0:
                req_inv = map_reqs.get(len_pre - 1, count_inv)
                if count_inv != req_inv:
                    return 0

            total_count = 0
            for index_num in range(n):
                if (bits_used & (1 << index_num)) == 0:
                    inv_next = count_inv
                    for inner_j in range(index_num + 1, n):
                        if (bits_used & (1 << inner_j)) != 0:
                            inv_next += 1
                    total_count = (total_count + count_permutations(len_pre + 1, inv_next, bits_used | (1 << index_num))) % CONST_MOD
            return total_count

        return count_permutations(0, 0, 0)