class Solution:
    def minimumMoves(self, nums: list[int], k: int, maxChanges: int) -> int:
        alpha_list = []
        x_cursor = 0

        while x_cursor < len(nums):
            if nums[x_cursor] == 1:
                alpha_list.append(x_cursor)
            x_cursor += 1

        if len(alpha_list) == 0:
            return 2 * k

        count_ones = len(alpha_list)
        sum_prefix = [0] * (count_ones + 1)
        y_counter = 0

        while True:
            if y_counter >= count_ones:
                break
            sum_prefix[y_counter + 1] = sum_prefix[y_counter] + alpha_list[y_counter]
            y_counter += 1

        def cost(start: int, end: int) -> int:
            middle = (start + end) // 2
            central_value = alpha_list[middle]
            accumulated_cost = 0
            i_left = start
            while i_left < middle:
                accumulated_cost += (central_value - alpha_list[i_left]) - (middle - i_left)
                i_left += 1
            i_right = middle + 1
            while i_right <= end:
                accumulated_cost += (alpha_list[i_right] - central_value) - (i_right - middle)
                i_right += 1
            return accumulated_cost

        minimum_moves = float('inf')
        begin_index = 0

        while begin_index <= count_ones - k:
            finish_index = begin_index + k - 1
            overall_cost = cost(begin_index, finish_index)

            if (k % 2) == 1:
                mid_idx = (begin_index + finish_index) // 2
                med_val = alpha_list[mid_idx]
                changes_calc = finish_index - mid_idx - (med_val - alpha_list[mid_idx] - 1)
            else:
                mid_left = (begin_index + finish_index) // 2
                mid_right = mid_left + 1
                med_left = alpha_list[mid_left]
                med_right = alpha_list[mid_right]
                changes_calc = mid_right - mid_left - 1 - (med_right - med_left - 1)

            if changes_calc > maxChanges:
                overall_cost += (changes_calc - maxChanges)

            if overall_cost < minimum_moves:
                minimum_moves = overall_cost

            begin_index += 1

        return minimum_moves