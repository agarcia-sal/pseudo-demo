import math

def max_fill(grid, capacity):
    total_uses = 0
    for well in grid:
        water_units = sum(well)
        uses_for_well = math.ceil(water_units / capacity)
        total_uses += uses_for_well
    return total_uses