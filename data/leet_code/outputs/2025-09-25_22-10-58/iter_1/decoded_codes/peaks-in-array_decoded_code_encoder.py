from bisect import bisect_left, bisect_right, insort

class Solution:
    def countOfPeaks(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        def is_peak(i: int) -> bool:
            # A peak is greater than its immediate neighbors
            return nums[i] > nums[i - 1] and nums[i] > nums[i + 1]

        peaks = []
        n = len(nums)
        # Collect initial peaks (indices from 1 to n-2)
        for i in range(1, n - 1):
            if is_peak(i):
                peaks.append(i)

        result = []
        for query in queries:
            if query[0] == 1:
                li, ri = query[1], query[2]
                # Find how many peak indices are in [li+1, ri-1] range by insertion positions
                left_index = bisect_left(peaks, li + 1)
                right_index = bisect_right(peaks, ri - 1) - 1
                count = max(0, right_index - left_index + 1)
                result.append(count)
            else:
                indexi, vali = query[1], query[2]
                if nums[indexi] == vali:
                    continue
                nums[indexi] = vali
                start = max(1, indexi - 1)
                end = min(n - 2, indexi + 1)
                for i in range(start, end + 1):
                    peak = is_peak(i)
                    idx = bisect_left(peaks, i)
                    in_peaks = (idx < len(peaks) and peaks[idx] == i)
                    if peak:
                        if not in_peaks:
                            insort(peaks, i)
                    else:
                        if in_peaks:
                            peaks.pop(idx)
        return result