from bisect import bisect_left, bisect_right

class Solution:
    def countOfPeaks(self, nums, queries):
        def is_peak(x):
            return nums[x] > nums[x - 1] and nums[x] > nums[x + 1]

        peak_positions = []
        n = len(nums)
        for idx in range(1, n - 1):
            if is_peak(idx):
                peak_positions.append(idx)

        outputs = []
        for query in queries:
            if query[0] == 1:
                left_bound = query[1]
                right_bound = query[2]
                # Find left insert position for left_bound + 1 (strictly >= left_bound+1)
                lpos = bisect_left(peak_positions, left_bound + 1)
                # Find right insert position for right_bound (strictly > right_bound)
                rpos = bisect_right(peak_positions, right_bound) - 1
                if rpos < lpos:
                    outputs.append(0)
                else:
                    outputs.append(rpos - lpos + 1)
            else:
                pos_chg, val_chg = query[1], query[2]
                if nums[pos_chg] == val_chg:
                    continue
                nums[pos_chg] = val_chg
                check_start = max(1, pos_chg - 1)
                check_end = min(n - 2, pos_chg + 1)
                for i in range(check_start, check_end + 1):
                    currently_peak = is_peak(i)
                    # Binary search to find i in peak_positions
                    left, right = 0, len(peak_positions) - 1
                    found_index = -1
                    while left <= right:
                        mid = (left + right) // 2
                        if peak_positions[mid] == i:
                            found_index = mid
                            break
                        elif peak_positions[mid] < i:
                            left = mid + 1
                        else:
                            right = mid - 1
                    if currently_peak:
                        if found_index == -1:
                            insert_pos = bisect_left(peak_positions, i)
                            peak_positions.insert(insert_pos, i)
                    else:
                        if found_index != -1:
                            peak_positions.pop(found_index)
        return outputs