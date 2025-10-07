import math

def max_fill(grid, capacity):
    total_lowerings = 0
    for arr in grid:
        sum_of_units = sum(arr)
        lowers_for_this_well = math.ceil(sum_of_units / capacity)
        total_lowerings += lowers_for_this_well
    return total_lowerings