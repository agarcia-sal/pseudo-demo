def max_fill(grid, capacity):
    import math
    total_calls = 0
    for each_index_row in range(len(grid)):
        current_row = grid[each_index_row]
        sum_water_units = 0
        for each_index_col in range(len(current_row)):
            sum_water_units += current_row[each_index_col]
        calls_for_row = math.ceil(sum_water_units / capacity)
        total_calls += calls_for_row
    return total_calls