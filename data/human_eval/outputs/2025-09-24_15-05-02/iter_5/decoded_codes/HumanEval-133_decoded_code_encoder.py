import math

def sum_squares(lst):
    squared = 0
    for i in lst:
        rounded_value = math.ceil(i)
        squared += rounded_value ** 2
    return squared