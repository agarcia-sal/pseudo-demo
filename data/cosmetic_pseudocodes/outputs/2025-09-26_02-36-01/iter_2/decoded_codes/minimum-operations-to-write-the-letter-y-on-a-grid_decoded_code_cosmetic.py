from collections import defaultdict
from math import inf

class Solution:
    def minimumOperationsToWriteY(self, grid):
        length_be = len(grid)
        midpoint = length_be // 2
        positions = set()

        idx = 0
        while idx <= midpoint:
            positions.add((idx, idx))
            idx += 1

        idx = 0
        while idx <= midpoint:
            positions.add((idx, (length_be - 1) - idx))
            idx += 1

        row_counter = midpoint
        while row_counter <= length_be - 1:
            positions.add((row_counter, midpoint))
            row_counter += 1

        y_group_counts = defaultdict(int)
        not_y_group_counts = defaultdict(int)

        r = 0
        while r < length_be:
            c = 0
            while c < length_be:
                if (r, c) in positions:
                    current_val = grid[r][c]
                    y_group_counts[current_val] += 1
                else:
                    val_alt = grid[r][c]
                    not_y_group_counts[val_alt] += 1
                c += 1
            r += 1

        minimum_ops = inf

        y_val_counter = 0
        while y_val_counter <= 2:
            non_y_val_counter = 0
            while non_y_val_counter <= 2:
                if y_val_counter != non_y_val_counter:
                    total_y = sum(y_group_counts.values())
                    y_val_count = y_group_counts.get(y_val_counter, 0)
                    total_not_y = sum(not_y_group_counts.values())
                    not_y_val_count = not_y_group_counts.get(non_y_val_counter, 0)
                    ops_needed = (total_y - y_val_count) + (total_not_y - not_y_val_count)

                    if ops_needed < minimum_ops:
                        minimum_ops = ops_needed
                non_y_val_counter += 1
            y_val_counter += 1

        return minimum_ops