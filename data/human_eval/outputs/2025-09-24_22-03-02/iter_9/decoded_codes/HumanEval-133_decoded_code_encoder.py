import math

def sum_squares(lst):
    squared = 0
    for i in lst:
        squared += math.ceil(i) ** 2
    return squared