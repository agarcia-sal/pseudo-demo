from collections import defaultdict

class Solution:
    def sumOfGoodSubsequences(self, nums):
        CONST_modulus = 1_000_000_000 + 7
        map_f = defaultdict(int)
        map_g = defaultdict(int)

        idx_i = 0
        while idx_i < len(nums):
            curr_val = nums[idx_i]

            map_g[curr_val] = (map_g[curr_val] + 1) % CONST_modulus
            map_f[curr_val] = (map_f[curr_val] + curr_val) % CONST_modulus

            tmp_calc = (map_f[curr_val - 1] + map_g[curr_val - 1] * curr_val) % CONST_modulus
            map_f[curr_val] = (map_f[curr_val] + tmp_calc) % CONST_modulus

            map_g[curr_val] = (map_g[curr_val] + map_g[curr_val - 1]) % CONST_modulus

            tmp_calc_2 = (map_f[curr_val + 1] + map_g[curr_val + 1] * curr_val) % CONST_modulus
            map_f[curr_val] = (map_f[curr_val] + tmp_calc_2) % CONST_modulus

            map_g[curr_val] = (map_g[curr_val] + map_g[curr_val + 1]) % CONST_modulus

            idx_i += 1

        summation_result = 0
        iterator_vals = list(map_f.values())
        idx_j = 0
        while idx_j < len(iterator_vals):
            summation_result += iterator_vals[idx_j]
            idx_j += 1

        ret_val = summation_result % CONST_modulus
        return ret_val