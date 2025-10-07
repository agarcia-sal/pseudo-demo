import math

def max_fill(grid, capacity):
    total_lowerings = 0

    for well_row in grid:
        water_units = sum(well_row)
        lowers_for_well = math.ceil(water_units / capacity)
        total_lowerings += lowers_for_well

    return total_lowerings