from bisect import bisect_left, bisect_right

class Solution:
    def countOfPeaks(self, nums, queries):
        def check_if_peak(pos):
            return nums[pos] > nums[pos - 1] and nums[pos] > nums[pos + 1]

        def insert_into_sorted(lst, val):
            low, high = 0, len(lst)
            while low < high:
                mid = (low + high) // 2
                if lst[mid] < val:
                    low = mid + 1
                else:
                    high = mid
            lst.insert(low, val)

        def left_bound(lst, target):
            start, end = 0, len(lst)
            while start < end:
                center = (start + end) // 2
                if lst[center] < target:
                    start = center + 1
                else:
                    end = center
            return start

        def right_bound(lst, target):
            beg, en = 0, len(lst)
            while beg < en:
                c = (beg + en) // 2
                if lst[c] <= target:
                    beg = c + 1
                else:
                    en = c
            return beg

        peak_positions = []

        def collect_peaks(start_index, end_index):
            if start_index > end_index:
                return
            if check_if_peak(start_index):
                peak_positions.append(start_index)
            collect_peaks(start_index + 1, end_index)

        if len(nums) >= 3:
            collect_peaks(1, len(nums) - 2)

        collected_results = []

        def process_all_queries(idx):
            if idx >= len(queries):
                return

            current_query = queries[idx]

            if current_query[0] == 1:
                left_v, right_v = current_query[1], current_query[2]

                left_pos = left_bound(peak_positions, left_v + 1)
                right_pos = right_bound(peak_positions, right_v - 1) - 1

                if right_pos < left_pos:
                    collected_results.append(0)
                else:
                    collected_results.append(right_pos - left_pos + 1)
            else:
                upd_index, upd_value = current_query[1], current_query[2]

                if nums[upd_index] == upd_value:
                    process_all_queries(idx + 1)
                    return

                nums[upd_index] = upd_value

                def update_peak_at(pos):
                    if pos < 1 or pos > len(nums) - 2:
                        return
                    currently_peak = check_if_peak(pos)

                    # Binary search for pos in peak_positions
                    lowi, highi = 0, len(peak_positions) - 1
                    exists_index = -1
                    while lowi <= highi:
                        midx = (lowi + highi) // 2
                        if peak_positions[midx] == pos:
                            exists_index = midx
                            break
                        elif peak_positions[midx] < pos:
                            lowi = midx + 1
                        else:
                            highi = midx - 1

                    if currently_peak:
                        if exists_index == -1:
                            insert_into_sorted(peak_positions, pos)
                    else:
                        if exists_index != -1:
                            peak_positions.pop(exists_index)

                start_scan = max(1, upd_index - 1)
                end_scan = min(len(nums) - 2, upd_index + 1)

                def loop_update(position):
                    if position > end_scan:
                        return
                    update_peak_at(position)
                    loop_update(position + 1)

                loop_update(start_scan)

            process_all_queries(idx + 1)

        process_all_queries(0)
        return collected_results