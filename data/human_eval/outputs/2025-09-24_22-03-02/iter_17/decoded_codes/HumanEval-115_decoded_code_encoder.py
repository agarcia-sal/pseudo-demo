import math

def max_fill(grid, capacity):
    total_times = 0
    for arr in grid:
        sum_units = 0
        for unit in arr:
            sum_units += unit
        required_times = math.ceil(sum_units / capacity)
        total_times += required_times
    return total_times