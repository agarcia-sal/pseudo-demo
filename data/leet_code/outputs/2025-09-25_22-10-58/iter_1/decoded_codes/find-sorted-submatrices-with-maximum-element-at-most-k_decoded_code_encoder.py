from typing import List

class Solution:
    def countSubmatrices(self, grid: List[List[int]], k: int) -> int:
        m = len(grid)
        n = len(grid[0]) if m > 0 else 0
        count = 0

        def is_valid_submatrix(submatrix: List[List[int]]) -> bool:
            for row in submatrix:
                for val in row:
                    if val > k:
                        return False
            return True

        def is_sorted_submatrix(submatrix: List[List[int]]) -> bool:
            for row in submatrix:
                for j in range(1, len(row)):
                    if row[j] > row[j - 1]:
                        return False
            return True

        for x1 in range(m):
            for y1 in range(n):
                for x2 in range(x1, m):
                    for y2 in range(y1, n):
                        submatrix = [row[y1:y2+1] for row in grid[x1:x2+1]]
                        if is_valid_submatrix(submatrix) and is_sorted_submatrix(submatrix):
                            count += 1

        return count