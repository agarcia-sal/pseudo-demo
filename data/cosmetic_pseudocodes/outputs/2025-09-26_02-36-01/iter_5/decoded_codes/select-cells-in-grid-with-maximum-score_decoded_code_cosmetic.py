from typing import List, Set

class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        max_sum = 0

        def backtrack(r: int, seen: Set[int], total: int):
            nonlocal max_sum
            if r == len(grid):
                if max_sum < total:
                    max_sum = total
                return
            else:
                # The pseudocode has backtrack(r + (1 - 0), ...), which is effectively r+1
                backtrack(r + 1, seen, total)
                def loop_elements(i: int):
                    if i == len(grid[r]):
                        return
                    else:
                        val_ = grid[r][i]
                        if val_ not in seen:
                            seen.add(val_)
                            backtrack(r + 1, seen, total + val_)
                            seen.remove(val_)
                        loop_elements(i + 1)
                loop_elements(0)

        def descending_sort(lst: List[int], start: int):
            if start >= len(lst) - 1:
                return
            else:
                max_idx = start
                def find_max(j: int, current_max_idx: int) -> int:
                    if j == len(lst):
                        return current_max_idx
                    else:
                        if lst[j] > lst[current_max_idx]:
                            return find_max(j + 1, j)
                        else:
                            return find_max(j + 1, current_max_idx)
                max_pos = find_max(start + 1, max_idx)
                if max_pos != start:
                    lst[start], lst[max_pos] = lst[max_pos], lst[start]
                descending_sort(lst, start + 1)

        idx_ = 0
        while idx_ < len(grid):
            descending_sort(grid[idx_], 0)
            idx_ += 1

        max_sum = 0
        backtrack(0, set(), 0)
        return max_sum