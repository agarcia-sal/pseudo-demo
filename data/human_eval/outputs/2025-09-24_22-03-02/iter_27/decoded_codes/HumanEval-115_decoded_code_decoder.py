import math

def max_fill(grid, capacity):
    total_lowers = 0
    index_row = 0
    while index_row < len(grid):
        current_row = grid[index_row]
        sum_units = 0
        index_unit = 0
        while index_unit < len(current_row):
            sum_units += current_row[index_unit]
            index_unit += 1
        lowers_for_row = math.ceil(sum_units / capacity)
        total_lowers += lowers_for_row
        index_row += 1
    return total_lowers