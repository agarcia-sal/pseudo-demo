import math

def max_fill(grid, capacity):
    total_raises = 0
    for arr in grid:
        water_units = sum(arr)
        raises_for_well = math.ceil(water_units / capacity)
        total_raises += raises_for_well
    return total_raises