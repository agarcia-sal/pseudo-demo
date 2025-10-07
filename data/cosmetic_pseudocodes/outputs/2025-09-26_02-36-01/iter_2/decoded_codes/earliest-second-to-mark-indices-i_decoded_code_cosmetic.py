from typing import List

class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        length_nums = len(nums)
        length_changes = len(changeIndices)

        def can_mark_by_second(limit: int) -> bool:
            last_seen = [-1] * length_nums
            index_counter = 0
            while index_counter < limit:
                pos = changeIndices[index_counter] - 1
                last_seen[pos] = index_counter
                index_counter += 1

            decrement_pool = 0
            marked = set()
            idx = 0
            while idx < limit:
                position = changeIndices[idx] - 1
                if position not in marked:
                    if last_seen[position] == idx:
                        if nums[position] <= decrement_pool:
                            decrement_pool -= nums[position]
                            marked.add(position)
                        else:
                            return False
                    else:
                        decrement_pool += 1
                else:
                    decrement_pool += 1
                idx += 1

            return len(marked) == length_nums

        start, end = 0, length_changes + 1
        while start < end:
            mid_point = (start + end) // 2
            if can_mark_by_second(mid_point):
                end = mid_point
            else:
                start += 1

        return start if start <= length_changes else -1