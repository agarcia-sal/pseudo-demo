import math

def sum_squares(lst) -> int:
    squared = 0
    for index in range(len(lst)):
        element = lst[index]
        ceil_value = math.ceil(element)
        squared += ceil_value * ceil_value
    return squared