from bisect import bisect_left, bisect_right

class Solution:
    def countOfPeaks(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        def is_peak(j: int) -> bool:
            return nums[j] > nums[j - 1] and nums[j] > nums[j + 1]

        def binary_left_insert_pos(arr: list[int], val: int) -> int:
            # returns leftmost position to insert val to keep arr sorted
            return bisect_left(arr, val)

        def binary_right_insert_pos(arr: list[int], val: int) -> int:
            # returns rightmost position to insert val to keep arr sorted
            return bisect_right(arr, val)

        acc_result = []
        peak_indices = []

        def loop_peaks_build(k: int, upper_limit: int):
            if k > upper_limit:
                return
            if is_peak(k):
                peak_indices.append(k)
            loop_peaks_build(k + 1, upper_limit)

        loop_peaks_build(1, len(nums) - 2)

        def process_queries(idx: int):
            if idx >= len(queries):
                return

            query_curr = queries[idx]
            type_flag = query_curr[0]

            if type_flag == 1:
                left_bound, right_bound = query_curr[1], query_curr[2]
                left_pos = binary_left_insert_pos(peak_indices, left_bound + 1)
                right_pos = binary_right_insert_pos(peak_indices, right_bound) - 1
                count_peaks_in_range = right_pos - left_pos if right_pos >= left_pos else 0
                acc_result.append(count_peaks_in_range)
            else:
                target_index, new_value = query_curr[1], query_curr[2]
                if nums[target_index] == new_value:
                    process_queries(idx + 1)
                    return
                nums[target_index] = new_value

                def update_peaks(m: int, upper_m: int):
                    if m > upper_m:
                        return
                    curr_is_peak = is_peak(m)
                    # find if m in peak_indices
                    pos = binary_left_insert_pos(peak_indices, m)
                    contains_m = (pos < len(peak_indices) and peak_indices[pos] == m)
                    if curr_is_peak:
                        if not contains_m:
                            peak_indices.insert(pos, m)
                    else:
                        if contains_m:
                            peak_indices.pop(pos)
                    update_peaks(m + 1, upper_m)

                low_range = max(1, target_index - 1)
                high_range = min(len(nums) - 2, target_index + 1)
                update_peaks(low_range, high_range)

            process_queries(idx + 1)

        process_queries(0)

        return acc_result