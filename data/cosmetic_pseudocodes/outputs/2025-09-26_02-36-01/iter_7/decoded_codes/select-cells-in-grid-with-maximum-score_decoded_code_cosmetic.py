from typing import List, Set

class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        max_result = 0

        def traverse(idx: int, picked: Set[int], accum: int) -> None:
            nonlocal max_result
            if not (idx < len(grid)):
                if max_result < accum:
                    max_result = accum
                return
            traverse(idx + 1, picked, accum)
            pos = 1
            while pos < len(grid[idx]):
                element = grid[idx][pos]
                if element not in picked:
                    picked.add(element)
                    traverse(idx + 1, picked, accum + element)
                    picked.remove(element)
                pos += 1

        i = len(grid) - 1
        while i >= 0:
            j = 1
            while j < len(grid[i]):
                if grid[i][j - 1] < grid[i][j]:
                    tmp = grid[i][j - 1]
                    grid[i][j - 1] = grid[i][j]
                    grid[i][j] = tmp
                    j = 0
                j += 1
            i -= 1

        traverse(0, set(), 0)
        return max_result