import math

def sum_squares(lst):
    squared = 0
    for element in lst:
        rounded_element = math.ceil(element)
        squared += rounded_element ** 2
    return squared