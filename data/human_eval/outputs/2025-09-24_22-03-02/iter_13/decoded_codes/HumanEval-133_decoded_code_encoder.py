import math

def sum_squares(lst):
    squared = 0
    for i in lst:
        ceil_value = math.ceil(i)
        square_value = ceil_value * ceil_value
        squared += square_value
    return squared