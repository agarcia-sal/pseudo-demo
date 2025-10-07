from bisect import bisect_left, bisect_right

class Solution:
    def countOfPeaks(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        def is_peak(h: int) -> bool:
            a = nums[h]
            b = nums[h - 1]
            c = nums[h + 1]
            return (b < a) and (a > c)

        peaks = []
        n = len(nums)
        for d in range(1, n - 1):
            if is_peak(d):
                peaks.append(d)

        output = []

        def insert_sorted(x: int, arr: list[int]):
            # Insert x into arr keeping it sorted (arr is sorted)
            pos = bisect_left(arr, x)
            arr.insert(pos, x)

        for item in queries:
            if item[0] == 1:
                start_val, end_val = item[1], item[2]

                def left_bound(val: int, arr: list[int]) -> int:
                    # smallest index i where arr[i] >= val
                    low, high = 0, len(arr)
                    while low < high:
                        mid = (low + high) // 2
                        if arr[mid] < val:
                            low = mid + 1
                        else:
                            high = mid
                    return low

                def right_bound(val: int, arr: list[int]) -> int:
                    # largest index i where arr[i] <= val
                    low, high = 0, len(arr)
                    while low < high:
                        mid = (low + high) // 2
                        if arr[mid] <= val:
                            low = mid + 1
                        else:
                            high = mid
                    return low - 1

                left_idx = left_bound(start_val, peaks)
                right_idx = right_bound(end_val, peaks)
                output.append(max(0, right_idx - left_idx + 1))
            else:
                pos, val = item[1], item[2]
                if nums[pos] == val:
                    continue
                nums[pos] = val

                from_i = max(1, pos - 1)
                to_i = min(n - 2, pos + 1)
                for j in range(from_i, to_i + 1):
                    peak_state = is_peak(j)
                    in_peaks = False
                    # check presence using binary search for efficiency
                    idx = bisect_left(peaks, j)
                    if idx < len(peaks) and peaks[idx] == j:
                        in_peaks = True

                    if peak_state and not in_peaks:
                        insert_sorted(j, peaks)
                    elif not peak_state and in_peaks:
                        peaks.pop(idx)
        return output