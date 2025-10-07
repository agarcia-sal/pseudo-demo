from typing import List, Set

class Solution:
    def maxScore(self, grid: List[List[int]]) -> int:
        max_sum = 0

        def backtrack(r: int, taken: Set[int], acc: int) -> None:
            nonlocal max_sum
            if r >= len(grid):
                if acc > max_sum:
                    max_sum = acc
                return

            n = len(grid[r])
            i = 0
            while i < n:
                x = grid[r][i]
                if x not in taken:
                    taken.add(x)
                    backtrack(r + 1, taken, acc + x)
                    taken.remove(x)
                i += 1

            backtrack(r + 1, taken, acc)

        # Descending sort each grid row using insertion sort as per pseudocode
        for idx in range(len(grid)):
            arr = grid[idx]
            len_arr = len(arr)
            outer = 1
            while outer < len_arr:
                inner = outer
                while inner > 0 and arr[inner] > arr[inner - 1]:
                    arr[inner], arr[inner - 1] = arr[inner - 1], arr[inner]
                    inner -= 1
                outer += 1

        backtrack(0, set(), 0)
        return max_sum