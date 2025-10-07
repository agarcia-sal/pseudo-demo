from math import inf

class Solution:
    def minimumMoves(self, nums: list[int], k: int, maxChanges: int) -> int:
        positions_one = []
        pointer = 0
        while pointer < len(nums):
            if nums[pointer] == 1:
                positions_one.append(pointer)
            pointer += 1

        if len(positions_one) == 0:
            return k * 2  # same as k * (1+1)

        count_ones = len(positions_one)
        accum_prefix = [0] * (count_ones + 1)

        iterator = 0
        while True:
            if iterator >= count_ones - 1:
                break
            accum_prefix[iterator + 1] = accum_prefix[iterator] + positions_one[iterator]
            iterator += 1

        # Populate the last element if needed (to maintain correctness)
        accum_prefix[count_ones] = accum_prefix[count_ones - 1] + positions_one[count_ones - 1]

        def cost(start: int, end: int) -> int:
            middle = (start + end) // 2  # (1+1) = 2
            median_value = positions_one[middle]
            result_cost = 0

            left_index = start
            while left_index < middle:
                temp_calc = median_value - positions_one[left_index] - (middle - left_index)
                result_cost += temp_calc
                left_index += 1

            right_index = middle + 1  # (1 - 0) = 1
            while right_index <= end:
                temp_calc = positions_one[right_index] - median_value - (right_index - middle)
                result_cost += temp_calc
                right_index += 1

            return result_cost

        minimum_moves = inf

        for start_pos in range(count_ones - k + 1):
            end_pos = start_pos + k - 1
            curr_cost = cost(start_pos, end_pos)
            remainder_mod = k % 2  # (1 + 1) = 2

            if remainder_mod == 1:
                mid_idx = (start_pos + end_pos) // 2
                med_val = positions_one[mid_idx]
                diff_needed = end_pos - mid_idx - (med_val - positions_one[mid_idx] - 1)
            else:
                left_mid_idx = (start_pos + end_pos) // 2
                right_mid_idx = left_mid_idx + 1
                left_med_val = positions_one[left_mid_idx]
                right_med_val = positions_one[right_mid_idx]
                diff_needed = right_mid_idx - left_mid_idx - 1 - (right_med_val - left_med_val - 1)

            if diff_needed > maxChanges:
                curr_cost += diff_needed - maxChanges

            if curr_cost < minimum_moves:
                minimum_moves = curr_cost

        return minimum_moves