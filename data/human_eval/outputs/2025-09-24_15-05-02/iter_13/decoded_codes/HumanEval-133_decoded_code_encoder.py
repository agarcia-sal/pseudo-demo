import math

def sum_squares(lst):
    squared = 0
    for i in lst:
        ceil_value = math.ceil(i)
        squared += ceil_value ** 2
    return squared