import math

def sum_squares(lst):
    squared = 0
    for i in range(len(lst)):
        element = lst[i]
        ceil_element = math.ceil(element)
        squared += ceil_element * ceil_element
    return squared