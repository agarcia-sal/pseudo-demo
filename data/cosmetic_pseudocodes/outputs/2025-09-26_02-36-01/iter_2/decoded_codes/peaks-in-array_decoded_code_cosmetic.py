from bisect import bisect_left, bisect_right

class Solution:
    def countOfPeaks(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        def is_peak(pos: int) -> bool:
            prev_val = nums[pos - 1]
            curr_val = nums[pos]
            next_val = nums[pos + 1]
            return (prev_val < curr_val) and (curr_val > next_val)

        peak_positions = []
        n = len(nums)
        for idx in range(1, n - 1):
            if is_peak(idx):
                peak_positions.append(idx)

        output_list = []
        for qry in queries:
            op_type = qry[0]
            if op_type == 1:
                start_bound = qry[1]
                end_bound = qry[2]

                # Find left_pos: first peak position >= start_bound + 1
                left_pos = bisect_left(peak_positions, start_bound + 1)
                # Find right_pos: last peak position <= end_bound - 1
                right_pos = bisect_right(peak_positions, end_bound - 1) - 1

                count_peaks = 0
                if right_pos >= left_pos and 0 <= left_pos < len(peak_positions) and 0 <= right_pos < len(peak_positions):
                    count_peaks = right_pos - left_pos + 1

                output_list.append(count_peaks)
            else:
                change_idx = qry[1]
                new_value = qry[2]

                if nums[change_idx] == new_value:
                    continue

                nums[change_idx] = new_value

                start_update = max(1, change_idx - 1)
                end_update = min(n - 2, change_idx + 1)

                for pos_update in range(start_update, end_update + 1):
                    currently_peak = is_peak(pos_update)

                    idx_in_peaks = bisect_left(peak_positions, pos_update)
                    found = (idx_in_peaks < len(peak_positions) and peak_positions[idx_in_peaks] == pos_update)

                    if currently_peak:
                        if not found:
                            peak_positions.insert(idx_in_peaks, pos_update)
                    else:
                        if found:
                            peak_positions.pop(idx_in_peaks)

        return output_list