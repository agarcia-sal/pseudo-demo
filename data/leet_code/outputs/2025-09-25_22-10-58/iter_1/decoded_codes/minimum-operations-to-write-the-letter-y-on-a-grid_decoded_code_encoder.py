from collections import Counter
from math import inf

class Solution:
    def minimumOperationsToWriteY(self, grid):
        n = len(grid)
        center = n // 2
        y_cells = set()

        for i in range(center + 1):
            y_cells.add((i, i))

        for i in range(center + 1):
            y_cells.add((i, n - i - 1))

        for i in range(center, n):
            y_cells.add((i, center))

        y_count = Counter(grid[r][c] for r, c in y_cells)
        non_y_count = Counter(grid[r][c] for r in range(n) for c in range(n) if (r, c) not in y_cells)

        min_operations = inf
        total_y = sum(y_count.values())
        total_non_y = sum(non_y_count.values())

        for y_val in range(3):
            for non_y_val in range(3):
                if y_val != non_y_val:
                    operations = total_y - y_count.get(y_val, 0) + total_non_y - non_y_count.get(non_y_val, 0)
                    if operations < min_operations:
                        min_operations = operations

        return min_operations