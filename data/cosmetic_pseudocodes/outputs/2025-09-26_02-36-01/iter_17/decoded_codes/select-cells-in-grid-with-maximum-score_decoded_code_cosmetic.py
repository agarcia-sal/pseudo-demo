from typing import List, Set

class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        global_max = 0

        # Sort each row in descending order in-place
        for line in grid:
            n = len(line)
            for i in range(n):
                for j in range(i + 1, n):
                    if line[j] > line[i]:
                        line[i], line[j] = line[j], line[i]

        def explore(r: int, taken: Set[int], aggregate: int):
            nonlocal global_max
            if r >= len(grid):
                if aggregate > global_max:
                    global_max = aggregate
                return

            explore(r + 1, taken, aggregate)

            for candidate in grid[r]:
                if candidate not in taken:
                    taken.add(candidate)
                    explore(r + 1, taken, aggregate + candidate)
                    taken.remove(candidate)

        explore(0, set(), 0)
        return global_max