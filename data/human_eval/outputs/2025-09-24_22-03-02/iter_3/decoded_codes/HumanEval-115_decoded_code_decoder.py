import math

def max_fill(grid, capacity):
    return sum(math.ceil(sum(well) / capacity) for well in grid)