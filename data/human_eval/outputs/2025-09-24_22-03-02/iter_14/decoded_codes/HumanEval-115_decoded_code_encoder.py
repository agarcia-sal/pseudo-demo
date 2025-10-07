import math

def max_fill(grid, capacity):
    total_lowerings = 0
    for arr in grid:
        water_units = 0
        for element in arr:
            if element == 1:
                water_units += 1
        lowers_for_arr = math.ceil(water_units / capacity)
        total_lowerings += lowers_for_arr
    return total_lowerings