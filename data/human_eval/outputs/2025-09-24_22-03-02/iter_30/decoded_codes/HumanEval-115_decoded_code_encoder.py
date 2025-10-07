import math
def max_fill(grid, capacity):
    total_lowerings = 0
    for arr in grid:
        sum_units = sum(arr)
        lowers_for_arr = math.ceil(sum_units / capacity)
        total_lowerings += lowers_for_arr
    return total_lowerings