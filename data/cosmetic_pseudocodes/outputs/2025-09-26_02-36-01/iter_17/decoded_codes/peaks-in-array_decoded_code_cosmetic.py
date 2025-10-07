from bisect import bisect_left, bisect_right

class Solution:
    def countOfPeaks(self, nums: list[int], queries: list[list[int]]) -> list[int]:
        def is_peak(pos: int) -> bool:
            curr_val = nums[pos]
            left_val = nums[pos - 1]
            right_val = nums[pos + 1]
            return left_val < curr_val > right_val

        peak_positions = []
        for idx in range(1, len(nums) - 1):
            if is_peak(idx):
                peak_positions.append(idx)

        output = []
        total_queries = len(queries)
        curr_q_idx = 0

        while curr_q_idx < total_queries:
            q = queries[curr_q_idx]
            if q[0] == 1:
                left_bound, right_bound = q[1], q[2]

                # upper_bound equivalent: first index in peak_positions where element > left_bound + 1 - 1
                # careful with +1 from pseudocode, use left_bound + 1 as in code
                l_insert_pos = bisect_right(peak_positions, left_bound + 1)
                # lower_bound equivalent: first index in peak_positions where element >= right_bound
                r_insert_pos = bisect_left(peak_positions, right_bound)
                p_index_left = l_insert_pos
                p_index_right = r_insert_pos - 1
                pos = p_index_right - p_index_left
                output.append(pos)

            else:
                pos, val = q[1], q[2]
                if nums[pos] == val:
                    curr_q_idx += 1
                    continue
                nums[pos] = val

                i_min = max(1, pos - 1)
                i_max = min(len(nums) - 2, pos + 1)

                for loop_i in range(i_min, i_max + 1):
                    def binary_search(arr: list[int], target: int) -> bool:
                        l, r = 0, len(arr) - 1
                        while l <= r:
                            m = (l + r) // 2
                            if arr[m] == target:
                                return True
                            elif arr[m] < target:
                                l = m + 1
                            else:
                                r = m - 1
                        return False

                    def insert_sorted(arr: list[int], val: int):
                        pos = bisect_left(arr, val)
                        arr.insert(pos, val)

                    def remove_sorted(arr: list[int], val: int):
                        l, r = 0, len(arr) - 1
                        pos = -1
                        while l <= r:
                            m = (l + r) // 2
                            if arr[m] == val:
                                pos = m
                                break
                            elif arr[m] < val:
                                l = m + 1
                            else:
                                r = m - 1
                        if pos != -1:
                            arr.pop(pos)

                    p_exists = binary_search(peak_positions, loop_i)
                    if is_peak(loop_i):
                        if not p_exists:
                            insert_sorted(peak_positions, loop_i)
                    else:
                        if p_exists:
                            remove_sorted(peak_positions, loop_i)
            curr_q_idx += 1

        return output