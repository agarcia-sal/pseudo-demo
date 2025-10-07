import math

def sum_squares(lst):
    squared = 0
    for i in lst:
        ceiling_value = math.ceil(i)
        squared += ceiling_value * ceiling_value
    return squared