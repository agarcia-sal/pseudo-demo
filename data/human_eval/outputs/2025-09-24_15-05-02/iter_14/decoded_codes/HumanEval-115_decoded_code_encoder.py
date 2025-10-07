import math

def max_fill(grid, capacity):
    total_to_lower_buckets = 0
    for well in grid:
        water_units = sum(well)
        lowers_for_well = math.ceil(water_units / capacity)
        total_to_lower_buckets += lowers_for_well
    return total_to_lower_buckets