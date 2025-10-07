class Solution:
    def numberOfPermutations(self, n, requirements):
        CONSTANT_BASE = 10
        CONSTANT_EXP = 9
        CONSTANT_ADD = 7

        def pow10(exp):
            if exp == 0:
                return 1
            else:
                return CONSTANT_BASE * pow10(exp - 1)

        MOD = pow10(CONSTANT_EXP) + CONSTANT_ADD

        dict_reqs = {}
        idxA = 0
        while idxA < len(requirements):
            req_pair = requirements[idxA]
            dict_reqs[req_pair[0]] = req_pair[1]
            idxA += 1

        def count_permutations(prefix_len, inv_count, bits_used):
            if prefix_len == n:
                def get_req_value(key):
                    return dict_reqs.get(key, 0)
                if inv_count == get_req_value(n - 1):
                    return 1
                else:
                    return 0
            else:
                def get_req_val_2(key):
                    return dict_reqs.get(key, key)
                if prefix_len > 0:
                    if inv_count != get_req_val_2(prefix_len - 1):
                        return 0

            total_count = 0

            def bit_mask(pos):
                return 1 << pos

            def update_inversions(num_val, used_bits_local):
                local_inv = inv_count
                idx_inner = num_val + 1
                while idx_inner < n:
                    if (used_bits_local & bit_mask(idx_inner)) != 0:
                        local_inv += 1
                    idx_inner += 1
                return local_inv

            def calculate_count(accum_count, add_val):
                return (accum_count + add_val) % MOD

            def rec_loop(i, accum):
                if i >= n:
                    return accum
                if (bits_used & bit_mask(i)) == 0:
                    new_inv = update_inversions(i, bits_used)
                    next_bits_used = bits_used | bit_mask(i)
                    accum = calculate_count(accum, count_permutations(prefix_len + 1, new_inv, next_bits_used))
                return rec_loop(i + 1, accum)

            return rec_loop(0, total_count)

        return count_permutations(0, 0, 0)