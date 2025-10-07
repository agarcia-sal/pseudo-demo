import math

def max_fill(grid, capacity):
    total_times = 0
    grid_length = len(grid)

    for i in range(grid_length):
        current_row = grid[i]
        row_length = len(current_row)
        row_sum = 0

        for j in range(row_length):
            row_sum += current_row[j]

        times_for_row = math.ceil(row_sum / capacity)
        total_times += times_for_row

    return total_times