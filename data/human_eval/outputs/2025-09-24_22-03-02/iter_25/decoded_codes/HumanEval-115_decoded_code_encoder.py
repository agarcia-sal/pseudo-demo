import math

def max_fill(grid, capacity):
    total_bucket_lowerings = 0
    for current_row in grid:
        sum_of_water_units = sum(current_row)
        bucket_lowerings_for_current_row = math.ceil(sum_of_water_units / capacity)
        total_bucket_lowerings += bucket_lowerings_for_current_row
    return total_bucket_lowerings