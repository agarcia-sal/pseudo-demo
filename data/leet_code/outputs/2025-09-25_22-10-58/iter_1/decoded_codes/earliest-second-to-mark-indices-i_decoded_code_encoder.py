from typing import List

class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        n = len(nums)
        m = len(changeIndices)

        def can_mark_by_second(k: int) -> bool:
            last_occurrence = [-1] * n
            for s in range(k):
                i = changeIndices[s] - 1
                last_occurrence[i] = s

            total_decrements_needed = sum(nums)
            available_decrements = 0
            marked_indices = set()

            for s in range(k):
                i = changeIndices[s] - 1
                if i not in marked_indices:
                    if last_occurrence[i] == s:
                        if nums[i] <= available_decrements:
                            available_decrements -= nums[i]
                            marked_indices.add(i)
                        else:
                            return False
                    else:
                        available_decrements += 1
                else:
                    available_decrements += 1

            return len(marked_indices) == n

        left, right = 0, m + 1
        while left < right:
            mid = (left + right) // 2
            if can_mark_by_second(mid):
                right = mid
            else:
                left += 1

        return left if left <= m else -1