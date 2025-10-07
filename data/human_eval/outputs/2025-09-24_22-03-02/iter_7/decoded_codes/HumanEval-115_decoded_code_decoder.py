import math

def max_fill(grid, capacity):
    total_times = 0
    for arr in grid:
        water_units = sum(arr)
        times = math.ceil(water_units / capacity)
        total_times += times
    return total_times