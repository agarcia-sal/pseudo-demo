from typing import List, Set

class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        # Preprocess each container:
        # Reverse each container and sort descending
        for i in range(len(grid)):
            container = grid[i]
            # reverse container
            reversed_container = container[::-1]
            # sort descending
            reversed_container.sort(reverse=True)
            grid[i] = reversed_container

        max_sum = 0

        def backtrack(index: int, visited: Set[int], accumulator: int):
            nonlocal max_sum
            if index >= len(grid):
                if accumulator > max_sum:
                    max_sum = accumulator
                return
            backtrack(index + 1, visited, accumulator)

            for element in grid[index]:
                if element not in visited:
                    visited.add(element)
                    backtrack(index + 1, visited, accumulator + element)
                    visited.remove(element)

        backtrack(0, set(), 0)
        return max_sum