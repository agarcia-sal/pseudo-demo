import math

def max_fill(grid, capacity):
    total_times = 0
    for arr in grid:
        water_units = 0
        for unit in arr:
            water_units += unit
        times_for_arr = math.ceil(water_units / capacity)
        total_times += times_for_arr
    return total_times