import math

def sum_squares(lst):
    squared = 0
    for i in lst:
        squared += math.ceil(i) * math.ceil(i)
    return squared