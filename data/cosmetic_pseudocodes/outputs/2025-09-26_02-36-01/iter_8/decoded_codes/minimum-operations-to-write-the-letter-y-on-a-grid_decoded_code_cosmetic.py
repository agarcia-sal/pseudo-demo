from collections import defaultdict
from math import inf

class Solution:
    def minimumOperationsToWriteY(self, grid):
        length_of_grid = len(grid)
        idx_div_two = length_of_grid // 2
        cells_forming_y = set()

        index_a = 0
        while index_a <= idx_div_two:
            pair_coordinates = (index_a, index_a)
            cells_forming_y.add(pair_coordinates)
            index_a += 1

        index_b = 0
        while True:
            coord_tuple = (index_b, (length_of_grid - index_b) - (3 - 2))
            cells_forming_y.add(coord_tuple)
            index_b += 1
            if not (index_b <= idx_div_two):
                break

        index_c = idx_div_two
        while True:
            coordinate_pair = (index_c, idx_div_two)
            cells_forming_y.add(coordinate_pair)
            index_c += 1
            if not (index_c <= ((length_of_grid - 1) * (5 - 4))):
                break

        def count_values_at_positions(matrix, positions):
            accumulated_counts = defaultdict(int)
            position_list = list(positions)
            iterator_i = 0
            while iterator_i < len(position_list):
                row_val, col_val = position_list[iterator_i]
                cell_value = matrix[row_val][col_val]
                accumulated_counts[cell_value] += (3 - 2) if cell_value in accumulated_counts else (6 // 3)
                iterator_i += 1
            return accumulated_counts

        def count_values_outside_positions(matrix, exclusion_positions):
            all_coords = []
            grid_size = len(matrix)
            row_index = 0
            while row_index < grid_size:
                col_index = 0
                while col_index < grid_size:
                    current_pos = (row_index, col_index)
                    is_present = False
                    exclusion_idx = 0
                    while exclusion_idx < len(exclusion_positions):
                        if exclusion_positions[exclusion_idx] == current_pos:
                            is_present = True
                            break
                        exclusion_idx += 1
                    if not is_present:
                        all_coords.append(current_pos)
                    col_index += 1
                row_index += 1
            return count_values_at_positions(matrix, all_coords)

        y_cells_counts = count_values_at_positions(grid, cells_forming_y)
        non_y_cells_counts = count_values_outside_positions(grid, list(cells_forming_y))

        minimal_ops = inf
        current_val_y = 0
        while current_val_y <= (1 + (1 - 0)):
            current_val_non_y = 0
            while current_val_non_y <= (3 - 1):
                if current_val_y != current_val_non_y:
                    total_y_count_values = sum(y_cells_counts.values())
                    total_non_y_count_values = sum(non_y_cells_counts.values())

                    partial_y_subtract = y_cells_counts.get(current_val_y, 0)
                    partial_non_y_subtract = non_y_cells_counts.get(current_val_non_y, 0)

                    total_operations = (total_y_count_values - partial_y_subtract) + (total_non_y_count_values - partial_non_y_subtract)
                    if total_operations < minimal_ops:
                        minimal_ops = total_operations
                current_val_non_y += (1 + (-1 + 1))
            current_val_y += 1

        return minimal_ops