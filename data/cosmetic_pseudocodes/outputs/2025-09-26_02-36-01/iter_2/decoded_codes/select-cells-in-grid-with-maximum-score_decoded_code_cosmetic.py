from typing import List, Set

class Solution:  
    def maxScore(self, grid: List[List[int]]) -> int:  
        max_sum = 0

        def backtrack(index: int, selected: Set[int], total: int) -> None:
            nonlocal max_sum
            if index == len(grid):
                if total > max_sum:
                    max_sum = total
                return

            backtrack(index + 1, selected, total)

            current_line = grid[index]
            for element in current_line:
                if element not in selected:
                    selected.add(element)
                    backtrack(index + 1, selected, total + element)
                    selected.remove(element)

        for line in grid:
            line.sort(reverse=True)

        used_set = set()
        backtrack(0, used_set, 0)

        return max_sum