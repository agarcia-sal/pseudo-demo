from collections import defaultdict

class Solution:
    def minimumOperationsToWriteY(self, grid):
        size = len(grid)
        mid = size // 2
        diagonal_coords = set()

        index = 0
        while index <= mid:
            diagonal_coords.add((index, index))
            index += 1

        index = 0
        while index <= mid:
            diagonal_coords.add((index, size - index - 1))
            index += 1

        row = mid
        while row <= size - 1:
            diagonal_coords.add((row, mid))
            row += 1

        y_positions_count = defaultdict(int)
        other_positions_count = defaultdict(int)

        r = 0
        while r < size:
            c = 0
            while c < size:
                cell_value = grid[r][c]
                if (r, c) in diagonal_coords:
                    y_positions_count[cell_value] += 1
                else:
                    other_positions_count[cell_value] += 1
                c += 1
            r += 1

        minimum_ops = float('inf')

        y_color = 0
        while y_color <= 2:
            non_y_color = 0
            while non_y_color <= 2:
                if y_color != non_y_color:
                    sum_y = sum(y_positions_count.values())
                    y_diff = sum_y - y_positions_count.get(y_color, 0)

                    sum_other = sum(other_positions_count.values())
                    non_y_diff = sum_other - other_positions_count.get(non_y_color, 0)

                    current_ops = y_diff + non_y_diff
                    if current_ops < minimum_ops:
                        minimum_ops = current_ops
                non_y_color += 1
            y_color += 1

        return minimum_ops