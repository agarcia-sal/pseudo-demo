from collections import defaultdict

class Solution:
    def sumOfGoodSubsequences(self, nums):
        modulus_value = 10**9 + 7
        f_map = defaultdict(int)
        g_map = defaultdict(int)

        length_nums = len(nums)

        def process_element(idx):
            if idx == length_nums:
                return

            current_num = nums[idx]

            updated_g_val = (g_map[current_num] + 1) % modulus_value
            updated_f_val = (f_map[current_num] + current_num) % modulus_value

            left_f_val = f_map.get(current_num - 1, 0)
            left_g_val = g_map.get(current_num - 1, 0)

            step1_f_val = left_f_val + (left_g_val * current_num)
            step1_f_val_mod = (updated_f_val + step1_f_val) % modulus_value

            step1_g_val_mod = (updated_g_val + left_g_val) % modulus_value

            right_f_val = f_map.get(current_num + 1, 0)
            right_g_val = g_map.get(current_num + 1, 0)

            step2_f_val = right_f_val + (right_g_val * current_num)
            step2_f_val_mod = (step1_f_val_mod + step2_f_val) % modulus_value

            step2_g_val_mod = (step1_g_val_mod + right_g_val) % modulus_value

            f_map[current_num] = step2_f_val_mod
            g_map[current_num] = step2_g_val_mod

            process_element(idx + 1)

        process_element(0)

        f_values_list = list(f_map.values())
        length_f_values = len(f_values_list)

        def sum_values(i):
            if i == length_f_values:
                return 0
            else:
                return f_values_list[i] + sum_values(i + 1)

        total_sum_values = sum_values(0)
        final_answer = total_sum_values % modulus_value

        return final_answer