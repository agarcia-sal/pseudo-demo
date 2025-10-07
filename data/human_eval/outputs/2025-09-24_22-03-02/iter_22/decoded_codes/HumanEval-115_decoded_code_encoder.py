def max_fill(grid, capacity):
    total_lowerings = 0
    for current_row in grid:
        sum_units = sum(current_row)
        if sum_units % capacity == 0:
            lowers_for_row = sum_units // capacity
        else:
            lowers_for_row = (sum_units // capacity) + 1
        total_lowerings += lowers_for_row
    return total_lowerings