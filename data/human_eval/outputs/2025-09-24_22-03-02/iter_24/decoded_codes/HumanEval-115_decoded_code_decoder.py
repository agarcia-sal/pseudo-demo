import math

def max_fill(grid, capacity):
    total_lowerings = 0
    index_row = 0
    while index_row < len(grid):
        current_row = grid[index_row]
        sum_in_row = 0
        index_element = 0
        while index_element < len(current_row):
            sum_in_row += current_row[index_element]
            index_element += 1
        times = math.ceil(sum_in_row / capacity)
        total_lowerings += times
        index_row += 1
    return total_lowerings