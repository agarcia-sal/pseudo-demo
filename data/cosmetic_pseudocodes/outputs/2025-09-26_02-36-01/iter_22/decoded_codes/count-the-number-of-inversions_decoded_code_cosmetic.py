class Solution:
    def numberOfPermutations(self, n, requirements):
        CONSTANT_MOD = 10**9 + 7
        mapping_dict = {}
        for pair_element in requirements:
            mapping_dict[pair_element[0]] = pair_element[1]

        def count_permutations(a_length, a_inversions, a_used):
            if a_length == n:
                val_check = mapping_dict.get(n - 1, 0)
                return 1 if a_inversions == val_check else 0

            if a_length > 0:
                val_check_two = mapping_dict.get(a_length - 1, a_inversions)
                if a_inversions != val_check_two:
                    return 0

            accumulator = 0
            for index_var in range(n):
                bit_check = a_used & (1 << index_var)
                if bit_check == 0:
                    new_inversion_count = a_inversions
                    for idx_inner in range(index_var + 1, n):
                        used_bit_inner = a_used & (1 << idx_inner)
                        if used_bit_inner != 0:
                            new_inversion_count += 1
                    accumulator = (accumulator + count_permutations(a_length + 1, new_inversion_count, a_used | (1 << index_var))) % CONSTANT_MOD
            return accumulator

        return count_permutations(0, 0, 0)