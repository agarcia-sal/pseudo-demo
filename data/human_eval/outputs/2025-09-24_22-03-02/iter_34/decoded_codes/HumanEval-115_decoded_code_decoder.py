import math

def max_fill(grid, capacity):
    total_lowerings = 0
    for i in range(len(grid)):
        current_row = grid[i]
        sum_water = 0
        for j in range(len(current_row)):
            sum_water += current_row[j]
        lowers_for_row = math.ceil(sum_water / capacity)
        total_lowerings += lowers_for_row
    return total_lowerings