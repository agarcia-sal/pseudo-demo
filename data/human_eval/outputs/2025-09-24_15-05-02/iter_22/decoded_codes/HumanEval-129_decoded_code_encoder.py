from typing import List

def minPath(grid: List[List[int]], path_length: int) -> List[int]:
    grid_size: int = len(grid)
    # Initialize with a large number greater than any possible grid value
    minimum_neighbor_value: int = grid_size * grid_size + 1

    for row_index in range(grid_size):
        for column_index in range(grid_size):
            if grid[row_index][column_index] == 1:
                neighbor_values: List[int] = []

                if row_index != 0:
                    neighbor_values.append(grid[row_index - 1][column_index])

                if column_index != 0:
                    neighbor_values.append(grid[row_index][column_index - 1])

                if row_index != grid_size - 1:
                    neighbor_values.append(grid[row_index + 1][column_index])

                if column_index != grid_size - 1:
                    neighbor_values.append(grid[row_index][column_index + 1])

                if neighbor_values:
                    current_min = min(neighbor_values)
                    if current_min < minimum_neighbor_value:
                        minimum_neighbor_value = current_min

    path_values: List[int] = []
    for step_index in range(path_length):
        if step_index % 2 == 0:
            path_values.append(1)
        else:
            path_values.append(minimum_neighbor_value)

    return path_values