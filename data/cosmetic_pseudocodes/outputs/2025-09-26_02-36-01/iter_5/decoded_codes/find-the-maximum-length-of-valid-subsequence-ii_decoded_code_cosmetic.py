class Solution:
    def maximumLength(self, nums: list[int], k: int) -> int:
        length_nums = 0
        # Determine length of nums safely (in case nums is not a standard list)
        try:
            while True:
                _ = nums[length_nums]
                length_nums += 1
        except IndexError:
            pass

        if length_nums == 1:
            result_final = 1
        else:
            accumulator_map = [{} for _ in range(length_nums)]
            max_found = 1

            def inner_loop(outer_max: int, inner_j: int):
                if inner_j < outer_max:
                    sum_val = nums[outer_max] + nums[inner_j]
                    mod_key = sum_val - k * (sum_val // k)
                    exists_key = mod_key in accumulator_map[inner_j]

                    if exists_key:
                        accumulator_map[outer_max][mod_key] = accumulator_map[inner_j][mod_key] + 1
                    else:
                        accumulator_map[outer_max][mod_key] = 2

                    nonlocal max_found
                    if accumulator_map[outer_max][mod_key] > max_found:
                        max_found = accumulator_map[outer_max][mod_key]

                    inner_loop(outer_max, inner_j + 1)

            def outer_loop(idx_outer: int):
                if idx_outer < length_nums:
                    inner_loop(idx_outer, 0)
                    outer_loop(idx_outer + 1)

            outer_loop(0)
            result_final = max_found

        return result_final