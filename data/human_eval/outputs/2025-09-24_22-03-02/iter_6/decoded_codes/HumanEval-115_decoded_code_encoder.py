import math

def max_fill(grid, capacity):
    total_times = 0
    for well_row in grid:
        water_units = sum(well_row)
        times_needed = math.ceil(water_units / capacity)
        total_times += times_needed
    return total_times