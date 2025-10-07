import math

def sum_squares(lst):
    squared = 0
    for element in lst:
        squared += math.ceil(element) ** 2
    return squared