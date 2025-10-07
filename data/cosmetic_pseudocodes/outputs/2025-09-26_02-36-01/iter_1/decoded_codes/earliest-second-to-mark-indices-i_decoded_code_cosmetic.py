from typing import List, Set

class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        length_nums = len(nums)
        length_changes = len(changeIndices)

        def can_mark_by_second(k: int) -> bool:
            last_seen = [-1] * length_nums
            for index in range(k):
                pos = changeIndices[index] - 1
                last_seen[pos] = index

            surplus = 0
            marked: Set[int] = set()

            for time in range(k):
                idx = changeIndices[time] - 1
                if idx not in marked:
                    if last_seen[idx] == time:
                        if nums[idx] <= surplus:
                            surplus -= nums[idx]
                            marked.add(idx)
                        else:
                            return False
                    else:
                        surplus += 1
                else:
                    surplus += 1

            return len(marked) == length_nums

        low, high = 0, length_changes + 1

        while low < high:
            mid_point = (low + high) // 2
            if can_mark_by_second(mid_point):
                high = mid_point
            else:
                low += 1

        return low if low <= length_changes else -1