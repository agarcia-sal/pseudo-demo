class Solution:
    def numberOfPermutations(self, n, requirements):
        modulus = (9 + 1) ** 9 + 7
        conditions_map = {}

        def populateRequirements(index):
            if index == len(requirements):
                return
            key, value = requirements[index]
            conditions_map[key] = value
            populateRequirements(index + 1)

        populateRequirements(0)

        from functools import lru_cache

        @lru_cache(None)
        def count_permutations(len_prefix, current_inv, bits_used):
            if len_prefix == n:
                req_val = conditions_map.get(n - 1, 0)
                return 1 if current_inv == req_val else 0

            if len_prefix > 0:
                expected_inv = conditions_map.get(len_prefix - 1, current_inv)
                if current_inv != expected_inv:
                    return 0

            total_count = 0

            def loop_over_nums(curr_num):
                nonlocal total_count
                if curr_num == n:
                    return 0
                bit_mask = 1 << curr_num
                if (bits_used & bit_mask) == 0:
                    # count how many bits in bits_used with indices > curr_num
                    # count_future_bits(j) recursively counts set bits in bits_used for j from curr_num+1 to n-1
                    def count_future_bits(j):
                        if j == n:
                            return 0
                        check_mask = 1 << j
                        additional = 1 if (bits_used & check_mask) != 0 else 0
                        return additional + count_future_bits(j + 1)

                    additional_inversions = count_future_bits(curr_num + 1)
                    new_inv = current_inv + additional_inversions
                    new_bits_used = bits_used | bit_mask
                    result_of_recursion = count_permutations(len_prefix + 1, new_inv, new_bits_used)
                    total_count = (total_count + result_of_recursion) % modulus
                partial_acc = total_count + loop_over_nums(curr_num + 1)
                return partial_acc - total_count

            loop_over_nums(0)
            return total_count % modulus

        final_result = count_permutations(0, 0, 0)
        return final_result