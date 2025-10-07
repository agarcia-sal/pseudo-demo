from typing import List, Set

class Solution:
    def earliestSecondToMarkIndices(self, nums: List[int], changeIndices: List[int]) -> int:
        p0 = len(nums)
        q1 = len(changeIndices)

        def can_mark_by_second(w7: int) -> bool:
            a3 = [-1] * p0  # last occurrence indices for positions, initialized to -1

            def proc_apply_last_occurrence(x9: int, y2: int) -> None:
                if x9 >= y2:
                    return
                c4 = changeIndices[x9] - 1
                a3[c4] = x9
                proc_apply_last_occurrence(x9 + 1, y2)

            proc_apply_last_occurrence(0, w7)

            acc6 = 0    # accumulation counter
            sx_set: Set[int] = set()
            idx_loop = 0

            while idx_loop < w7:
                posA = changeIndices[idx_loop] - 1
                if posA not in sx_set:
                    if a3[posA] == idx_loop:
                        if nums[posA] <= acc6:
                            acc6 -= nums[posA]
                            sx_set.add(posA)
                        else:
                            return False
                    else:
                        acc6 += 1
                else:
                    acc6 += 1
                idx_loop += 1

            return len(sx_set) == p0

        l7, r2 = 0, q1 + 1

        while l7 < r2:
            md = (l7 + r2) // 2
            if can_mark_by_second(md):
                r2 = md
            else:
                l7 += 1

        return l7 if l7 <= q1 else -1