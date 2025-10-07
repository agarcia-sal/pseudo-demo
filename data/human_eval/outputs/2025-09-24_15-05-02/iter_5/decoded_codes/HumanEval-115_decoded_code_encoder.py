import math

def max_fill(grid, capacity):
    total_lowerings = 0
    for well_row in grid:
        total_water_units = sum(well_row)
        times_to_lower_bucket = math.ceil(total_water_units / capacity)
        total_lowerings += times_to_lower_bucket
    return total_lowerings