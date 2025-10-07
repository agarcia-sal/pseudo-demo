from bisect import bisect_left, bisect_right, insort

class Solution:
    def countOfPeaks(self, nums: list[int], queries: list[list[int]]) -> list[int]:

        def is_peak(index: int) -> bool:
            return nums[index] > nums[index - 1] and nums[index] > nums[index + 1]

        peaks = []
        n = len(nums)
        for pos in range(1, n - 1):
            if is_peak(pos):
                peaks.append(pos)

        results = []
        for query in queries:
            if query[0] == 1:
                left_bound, right_bound = query[1], query[2]
                # Find left insertion position (left_pos): first peak strictly greater than left_bound
                left_pos = bisect_left(peaks, left_bound) + 1
                # Find right insertion position (right_pos): last peak strictly less than right_bound
                right_pos = bisect_right(peaks, right_bound) - 1
                results.append(max(0, right_pos - left_pos))
            else:
                idx, new_value = query[1], query[2]
                if nums[idx] == new_value:
                    continue
                nums[idx] = new_value
                start_pos = max(1, idx - 1)
                end_pos = min(n - 2, idx + 1)
                for pos in range(start_pos, end_pos + 1):
                    peak_status = is_peak(pos)
                    i = bisect_left(peaks, pos)
                    in_peaks = (i < len(peaks) and peaks[i] == pos)
                    if peak_status and not in_peaks:
                        insort(peaks, pos)
                    elif not peak_status and in_peaks:
                        peaks.pop(i)

        return results