import math

def max_fill(grid, capacity):
    total_times = 0
    for current_row in grid:
        sum_units = sum(current_row)
        division_result = sum_units / capacity
        times = math.ceil(division_result)
        total_times += times
    return total_times