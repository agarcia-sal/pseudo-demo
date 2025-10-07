from typing import List

class Solution:
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        def check_peak(pos: int) -> bool:
            return nums[pos] > nums[pos - 1] and nums[pos] > nums[pos + 1]

        peak_positions = []
        idx = 1
        n = len(nums)
        while idx <= n - 2:
            if check_peak(idx):
                peak_positions.append(idx)
            idx += 1

        def binary_left_insert(value: int) -> int:
            low, high = 0, len(peak_positions)
            while low < high:
                mid = (low + high) // 2
                if peak_positions[mid] < value:
                    low = mid + 1
                else:
                    high = mid
            return low

        def binary_right_insert(value: int) -> int:
            low, high = 0, len(peak_positions)
            while low < high:
                mid = (low + high) // 2
                if peak_positions[mid] <= value:
                    low = mid + 1
                else:
                    high = mid
            return low

        def exists_in_peaks(target: int) -> bool:
            left, right = 0, len(peak_positions) - 1
            while left <= right:
                mid = (left + right) // 2
                if peak_positions[mid] == target:
                    return True
                elif peak_positions[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1
            return False

        def insert_sorted(value: int):
            pos = binary_left_insert(value)
            peak_positions.insert(pos, value)

        def remove_sorted(value: int):
            pos = binary_left_insert(value)
            if pos < len(peak_positions) and peak_positions[pos] == value:
                peak_positions.pop(pos)

        answers = []

        def RECURSIVE_ITERATE(current: int, limit: int):
            if current > limit:
                return
            peak_check = check_peak(current)
            if peak_check:
                if not exists_in_peaks(current):
                    insert_sorted(current)
            else:
                if exists_in_peaks(current):
                    remove_sorted(current)
            RECURSIVE_ITERATE(current + 1, limit)

        def process_queries(j: int):
            if j >= len(queries):
                return
            current_query = queries[j]
            if current_query[0] == 1:
                l_val = current_query[1]
                r_val = current_query[2]
                left_pos = binary_left_insert(l_val + 1)
                right_pos = binary_right_insert(r_val) - 1
                if right_pos < left_pos:
                    answers.append(0)
                else:
                    answers.append(right_pos - left_pos + 1)
            else:
                update_idx = current_query[1]
                new_val = current_query[2]
                if nums[update_idx] == new_val:
                    process_queries(j + 1)
                    return
                nums[update_idx] = new_val
                start_pos = update_idx - 1
                if start_pos < 1:
                    start_pos = 1
                end_pos = update_idx + 1
                if end_pos > n - 2:
                    end_pos = n - 2
                RECURSIVE_ITERATE(start_pos, end_pos)
            process_queries(j + 1)

        process_queries(0)
        return answers