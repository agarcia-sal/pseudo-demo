import math

def max_fill(grid, capacity):
    total_lowerings = 0
    for row_index in range(len(grid)):
        current_row = grid[row_index]
        water_units = 0
        for element_index in range(len(current_row)):
            cell_value = current_row[element_index]
            water_units += cell_value
        required_lowerings = math.ceil(water_units / capacity)
        total_lowerings += required_lowerings
    return total_lowerings