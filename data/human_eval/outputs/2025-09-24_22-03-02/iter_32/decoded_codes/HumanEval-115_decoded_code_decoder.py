def max_fill(grid, capacity):
    import math
    total_lowerings = 0
    for i in range(len(grid)):
        current_row = grid[i]
        sum_units = 0
        for j in range(len(current_row)):
            sum_units += current_row[j]
        lowers_for_row = math.ceil(sum_units / capacity)
        total_lowerings += lowers_for_row
    return total_lowerings