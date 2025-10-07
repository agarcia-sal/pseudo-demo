from bisect import bisect_left, bisect_right

class Solution:
    def countOfPeaks(self, nums, queries):
        def is_peak(position):
            left_neighbor = nums[position - 1]
            current_value = nums[position]
            right_neighbor = nums[position + 1]
            condition_left = not (left_neighbor >= current_value)
            condition_right = current_value > right_neighbor
            return condition_left and condition_right

        def binary_left_insert(collection, target):
            # Using bisect_left for left insertion index
            return bisect_left(collection, target)

        def binary_right_insert(collection, target):
            # Using bisect_right for right insertion index
            return bisect_right(collection, target)

        def insert_in_sorted_list(sorted_list, value):
            pos = binary_left_insert(sorted_list, value)
            sorted_list.insert(pos, value)

        def remove_from_sorted_list(sorted_list, value):
            pos = binary_left_insert(sorted_list, value)
            if pos < len(sorted_list) and sorted_list[pos] == value:
                sorted_list.pop(pos)

        def is_in_sorted_list(sorted_list, value):
            pos = binary_left_insert(sorted_list, value)
            return pos < len(sorted_list) and sorted_list[pos] == value

        def process_indices(start_idx, end_idx, peaks_list):
            if start_idx > end_idx:
                return
            current_idx = start_idx
            if is_peak(current_idx):
                if not is_in_sorted_list(peaks_list, current_idx):
                    insert_in_sorted_list(peaks_list, current_idx)
            else:
                if is_in_sorted_list(peaks_list, current_idx):
                    remove_from_sorted_list(peaks_list, current_idx)
            process_indices(current_idx + 1, end_idx, peaks_list)

        peak_positions = []

        def initialize_peaks(current):
            if current > len(nums) - 2:
                return
            if is_peak(current):
                peak_positions.append(current)
            initialize_peaks(current + 1)

        if len(nums) >= 3:
            initialize_peaks(1)

        answers = []
        query_idx = 0
        n = len(nums)
        while query_idx < len(queries):
            individual_query = queries[query_idx]
            operation_type = individual_query[0]
            if operation_type == 1:
                left_val = individual_query[1]
                right_val = individual_query[2]
                left_pos = binary_left_insert(peak_positions, left_val + 1)
                right_pos = binary_right_insert(peak_positions, right_val) - 1
                count_diff = right_pos - left_pos
                answers.append(count_diff if count_diff >= 0 else 0)
            else:
                update_idx = individual_query[1]
                update_val = individual_query[2]
                if update_idx >= 0 and update_idx < n and nums[update_idx] != update_val:
                    nums[update_idx] = update_val
                    begin_range = max(1, update_idx - 1)
                    end_range = min(n - 2, update_idx + 1)
                    process_indices(begin_range, end_range, peak_positions)
            query_idx += 1

        return answers