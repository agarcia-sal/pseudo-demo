from typing import List


class Solution:
    def countOfPeaks(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        def is_peak(pos: int) -> bool:
            delta1 = nums[pos] - nums[pos - 1]
            delta2 = nums[pos] - nums[pos + 1]
            return delta1 > 0 and delta2 > 0

        alpha = []
        beta = 1
        while beta < len(nums) - 1:
            if is_peak(beta):
                alpha.append(beta)
            beta += 1

        omega = []
        mu = 0
        while True:
            if mu >= len(queries):
                break

            delta_query = queries[mu]
            lambda_val = delta_query[0]

            if lambda_val == 1:
                v1 = delta_query[1]
                v2 = delta_query[2]

                def left_insertion(a: int, arr: List[int]) -> int:
                    start_idx = 0
                    end_idx = len(arr)
                    while start_idx < end_idx:
                        mid_idx = start_idx + (end_idx - start_idx) // 2
                        if arr[mid_idx] >= a:
                            end_idx = mid_idx
                        else:
                            start_idx = mid_idx + 1
                    return start_idx

                def right_insertion(a: int, arr: List[int]) -> int:
                    left_idx = 0
                    right_idx = len(arr)
                    while left_idx < right_idx:
                        center_idx = left_idx + (right_idx - left_idx) // 2
                        if arr[center_idx] > a:
                            right_idx = center_idx
                        else:
                            left_idx = center_idx + 1
                    return left_idx

                left_inx = left_insertion(v1, alpha) + 1
                right_inx = right_insertion(v2, alpha) - 1
                omega.append(right_inx - left_inx)
            else:
                idx_mod = delta_query[1]
                val_mod = delta_query[2]

                if nums[idx_mod] == val_mod:
                    mu += 1
                    continue

                nums[idx_mod] = val_mod

                def insert_sorted(n: int, array: List[int]) -> List[int]:
                    pos_start = 0
                    pos_end = len(array)
                    while pos_start < pos_end:
                        pos_mid = pos_start + (pos_end - pos_start) // 2
                        if array[pos_mid] >= n:
                            pos_end = pos_mid
                        else:
                            pos_start = pos_mid + 1
                    return array[:pos_start] + [n] + array[pos_start:]

                def remove_element(n: int, array: List[int]) -> List[int]:
                    return [x for x in array if x != n]

                start_idx = idx_mod - 1 if (idx_mod - 1) > 1 else 1
                end_idx = idx_mod + 1 if (idx_mod + 1) < (len(nums) - 1) else len(nums) - 2

                i_cursor = start_idx
                while i_cursor <= end_idx:
                    if is_peak(i_cursor):
                        if i_cursor not in alpha:
                            alpha = insert_sorted(i_cursor, alpha)
                    else:
                        if i_cursor in alpha:
                            alpha = remove_element(i_cursor, alpha)
                    i_cursor += 1

            mu += 1

        return omega