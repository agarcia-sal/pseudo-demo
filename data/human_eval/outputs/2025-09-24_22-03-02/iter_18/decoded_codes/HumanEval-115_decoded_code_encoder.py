def max_fill(grid, capacity):
    import math
    total_drops = 0
    index_row = 0
    while index_row < len(grid):
        arr = grid[index_row]
        sum_units = 0
        index_element = 0
        while index_element < len(arr):
            sum_units += arr[index_element]
            index_element += 1
        drops_for_row = math.ceil(sum_units / capacity)
        total_drops += drops_for_row
        index_row += 1
    return total_drops