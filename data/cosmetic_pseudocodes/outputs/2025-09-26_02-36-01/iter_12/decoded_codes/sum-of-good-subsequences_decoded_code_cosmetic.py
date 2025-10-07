from collections import defaultdict

class Solution:
    def sumOfGoodSubsequences(self, nums):
        MOD_VALUE = 10**9 + 7
        map_f = defaultdict(int)
        map_g = defaultdict(int)

        def safe_get(d, key):
            return d.get(key, 0)

        def mod_add(target_map, key, val):
            old_val = safe_get(target_map, key)
            target_map[key] = (old_val + val) % MOD_VALUE

        index = 0
        length_nums = len(nums)
        while index < length_nums:
            current_val = nums[index]

            mod_add(map_g, current_val, 1)
            mod_add(map_f, current_val, current_val)

            left_key = current_val - 1
            left_f = safe_get(map_f, left_key)
            left_g = safe_get(map_g, left_key)
            increment_f1 = (left_f + left_g * current_val) % MOD_VALUE

            val_f_current = safe_get(map_f, current_val)
            val_f_current = (val_f_current + increment_f1) % MOD_VALUE
            map_f[current_val] = val_f_current

            val_g_current = safe_get(map_g, current_val)
            val_g_current = (val_g_current + left_g) % MOD_VALUE
            map_g[current_val] = val_g_current

            right_key = current_val + 1
            right_f = safe_get(map_f, right_key)
            right_g = safe_get(map_g, right_key)
            increment_f2 = (right_f + right_g * current_val) % MOD_VALUE

            map_f[current_val] = (map_f[current_val] + increment_f2) % MOD_VALUE
            map_g[current_val] = (map_g[current_val] + right_g) % MOD_VALUE

            index += 1

        accumulator = 0
        keys_list = list(map_f.keys())
        position = 0
        total_keys = len(keys_list)
        while True:
            if position >= total_keys:
                break
            current_key = keys_list[position]
            accumulator += map_f[current_key]
            position += 1

        output_result = accumulator % MOD_VALUE
        return output_result