import math

def max_fill(grid, c):
    return sum(math.ceil(sum(row) / c) for row in grid)