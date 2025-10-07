class Solution:
    def minimumOperationsToWriteY(self, grid):
        size = len(grid)
        mid = size // 2
        y_positions = set()

        idx = 0
        while idx <= mid:
            y_positions.add((idx, idx))
            idx += 1

        idx = 0
        while idx <= mid:
            y_positions.add((idx, size - idx - 1))
            idx += 1

        idx = mid
        while idx < size:
            y_positions.add((idx, mid))
            idx += 1

        y_counts = {0: 0, 1: 0, 2: 0}
        other_counts = {0: 0, 1: 0, 2: 0}

        for row in range(size):
            for col in range(size):
                if (row, col) in y_positions:
                    y_counts[grid[row][col]] += 1
                else:
                    other_counts[grid[row][col]] += 1

        best_result = float('inf')
        for val_in_y in [0, 1, 2]:
            for val_in_other in [0, 1, 2]:
                if val_in_y != val_in_other:
                    total_ops = (sum(y_counts.values()) - y_counts[val_in_y]) + (sum(other_counts.values()) - other_counts[val_in_other])
                    if total_ops < best_result:
                        best_result = total_ops

        return best_result