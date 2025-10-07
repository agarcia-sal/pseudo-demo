class Solution:
    def sumOfPowers(self, nums: list[int], k: int) -> int:
        constant_x = 10**9 + 7
        accumulator_var = 0

        def traverse_pairs(sequence: list[int]) -> int:
            def inner_loop(original_list: list[int], idx_param: int, current_min: int) -> int:
                min_value_var = current_min
                loop_index = idx_param + 1
                while loop_index < len(original_list):
                    diff_candidate = abs(original_list[idx_param] - original_list[loop_index])
                    if diff_candidate < min_value_var:
                        min_value_var = diff_candidate
                    loop_index += 1
                return min_value_var

            curr_index = 0
            min_diff = 10**9  # large initial minimum
            while curr_index < len(sequence) - 1:
                min_diff = inner_loop(sequence, curr_index, min_diff)
                curr_index += 1
            return min_diff

        combination_list = []

        def generate_combinations(source: list[int], combo_length: int, start_idx: int, picked_so_far: list[int]) -> None:
            current_depth = len(picked_so_far)
            if current_depth == combo_length:
                combination_list.append(picked_so_far)
                return
            pos = start_idx
            max_pos = len(source) - (combo_length - current_depth)
            while pos <= max_pos:
                generate_combinations(source, combo_length, pos + 1, picked_so_far + [source[pos]])
                pos += 1

        generate_combinations(nums, k, 0, [])

        combo_idx = 0
        while combo_idx < len(combination_list):
            min_diff_for_combo = traverse_pairs(combination_list[combo_idx])
            accumulator_var += min_diff_for_combo
            accumulator_var %= constant_x
            combo_idx += 1

        return accumulator_var