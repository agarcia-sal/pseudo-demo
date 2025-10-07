from math import floor
from typing import List

class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        length_nums = len(nums)
        length_changes = len(changeIndices)

        def can_mark_by_second(time_limit: int) -> bool:
            positions_last = [-1] * length_nums
            index_counter = 0
            while index_counter < time_limit:
                idx_adjusted = changeIndices[index_counter] - 1
                positions_last[idx_adjusted] = index_counter
                index_counter += 1

            required_decrements = sum(nums)

            decrements_remaining = 0
            marked_set = set()
            step_counter = 0

            while True:
                if not step_counter < time_limit:
                    break
                target_idx = changeIndices[step_counter] - 1
                if target_idx not in marked_set:
                    if positions_last[target_idx] == step_counter:
                        if nums[target_idx] <= decrements_remaining:
                            decrements_remaining -= nums[target_idx]
                            marked_set.add(target_idx)
                        else:
                            return False
                    else:
                        decrements_remaining += 1
                else:
                    decrements_remaining += 1
                step_counter += 1

            return len(marked_set) == length_nums

        low_bound, high_bound = 0, length_changes + 1

        def integer_divide(a: int, b: int) -> int:
            return floor(a / b)

        while low_bound < high_bound:
            middle = integer_divide(low_bound + high_bound, 2)
            if can_mark_by_second(middle):
                high_bound = middle
            else:
                low_bound += 1

        return low_bound if low_bound <= length_changes else -1