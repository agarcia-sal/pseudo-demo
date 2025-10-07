import math

def max_fill(grid, capacity):
    total_uses = 0

    for well in grid:
        units_of_water = sum(well)
        uses_for_well = math.ceil(units_of_water / capacity)
        total_uses += uses_for_well

    return total_uses