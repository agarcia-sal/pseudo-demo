from bisect import bisect_left, bisect_right

class Solution:
    def countOfPeaks(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        def is_peak(idx: int) -> bool:
            # idx is guaranteed to be between 1 and len(nums)-2 when called
            return nums[idx] > nums[idx - 1] and nums[idx] > nums[idx + 1]

        peaks = []
        n = len(nums)

        for idx in range(1, n - 1):
            if is_peak(idx):
                peaks.append(idx)

        output = []
        for query_item in queries:
            if query_item[0] == 1:
                li_val, ri_val = query_item[1], query_item[2]
                left_target = li_val + 1

                # Find left insertion position for left_target in peaks
                left_pos = bisect_left(peaks, left_target)

                # Find right insertion position for ri_val in peaks
                right_pos = bisect_right(peaks, ri_val)

                output.append(right_pos - left_pos)
            else:
                ind, val_repl = query_item[1], query_item[2]
                original_val = nums[ind]
                if original_val == val_repl:
                    continue  # No change, skip

                nums[ind] = val_repl

                start_idx = max(1, ind - 1)
                end_idx = min(n - 2, ind + 1)

                for s_idx in range(start_idx, end_idx + 1):
                    peak_status = is_peak(s_idx)

                    # Binary search peak status in peaks list
                    pos = bisect_left(peaks, s_idx)
                    found = (pos < len(peaks) and peaks[pos] == s_idx)

                    if peak_status:
                        if not found:
                            peaks.insert(pos, s_idx)
                    else:
                        if found:
                            peaks.pop(pos)

        return output