import math

def sum_squares(lst):
    squared = 0
    for i in lst:
        ceil_i = math.ceil(i)
        square_ceil_i = ceil_i * ceil_i
        squared += square_ceil_i
    return squared