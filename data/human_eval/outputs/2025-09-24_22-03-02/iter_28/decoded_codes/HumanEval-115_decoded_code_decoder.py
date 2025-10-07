def max_fill(grid, capacity):
    import math
    total_lowerings = 0
    for index_row in range(len(grid)):
        arr = grid[index_row]
        sum_of_units = 0
        for index_unit in range(len(arr)):
            sum_of_units = sum_of_units + arr[index_unit]
        lowered_times = math.ceil(sum_of_units / capacity)
        total_lowerings = total_lowerings + lowered_times
    return total_lowerings