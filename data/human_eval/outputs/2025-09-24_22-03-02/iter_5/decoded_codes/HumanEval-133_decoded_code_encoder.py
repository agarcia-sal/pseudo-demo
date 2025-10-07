import math

def sum_squares(lst):
    squared = 0
    for number in lst:
        ceiling_value = math.ceil(number)
        squared += ceiling_value ** 2
    return squared