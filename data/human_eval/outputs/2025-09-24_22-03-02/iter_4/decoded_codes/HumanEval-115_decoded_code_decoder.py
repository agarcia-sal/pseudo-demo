import math

def max_fill(grid, capacity):
    total_times = 0
    for arr in grid:
        water_units = sum(arr)
        times_for_well = math.ceil(water_units / capacity)
        total_times += times_for_well
    return total_times