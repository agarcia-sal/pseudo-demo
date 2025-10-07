class Solution:
    def maxValue(self, nums: list[int], k: int) -> int:
        power_val = 1
        bit_limit = 7
        index_counter = 0
        while index_counter < bit_limit:
            power_val *= 2
            index_counter += 1

        length_nums = len(nums)
        dimension_one = length_nums + 1
        dimension_two = k + 2
        dimension_three = power_val

        # Initialize state_array with False
        state_array = [[[False] * dimension_three for _ in range(dimension_two)] for __ in range(dimension_one)]
        state_array[0][0][0] = True

        outer_idx = 0
        while outer_idx < length_nums:
            middle_idx = 0
            while middle_idx <= k:
                inner_idx = 0
                while inner_idx < power_val:
                    carry_over = state_array[outer_idx][middle_idx][inner_idx]
                    if carry_over:
                        state_array[outer_idx + 1][middle_idx][inner_idx] = True
                        updated_bitset = inner_idx | nums[outer_idx]
                        if middle_idx + 1 < dimension_two:
                            state_array[outer_idx + 1][middle_idx + 1][updated_bitset] = True
                    inner_idx += 1
                middle_idx += 1
            outer_idx += 1

        # Initialize rev_state_array with False
        rev_state_array = [[[False] * dimension_three for _ in range(dimension_two)] for __ in range(dimension_one)]
        rev_state_array[length_nums][0][0] = True

        rev_outer = length_nums
        while rev_outer > 0:
            rev_middle = 0
            while rev_middle <= k:
                rev_inner = 0
                while rev_inner < power_val:
                    previous_rev_state = rev_state_array[rev_outer][rev_middle][rev_inner]
                    if previous_rev_state:
                        rev_state_array[rev_outer - 1][rev_middle][rev_inner] = True
                        combined_bits = rev_inner | nums[rev_outer - 1]
                        if rev_middle + 1 < dimension_two:
                            rev_state_array[rev_outer - 1][rev_middle + 1][combined_bits] = True
                    rev_inner += 1
                rev_middle += 1
            rev_outer -= 1

        maximum_result = 0
        mid_point_start = k
        mid_point_end = length_nums - k
        mid_pos = mid_point_start
        while mid_pos < mid_point_end:
            val_x = 0
            while val_x < power_val:
                if state_array[mid_pos][k][val_x]:
                    val_y = 0
                    while val_y < power_val:
                        if rev_state_array[mid_pos][k][val_y]:
                            candidate_val = val_x ^ val_y
                            if candidate_val > maximum_result:
                                maximum_result = candidate_val
                        val_y += 1
                val_x += 1
            mid_pos += 1

        return maximum_result