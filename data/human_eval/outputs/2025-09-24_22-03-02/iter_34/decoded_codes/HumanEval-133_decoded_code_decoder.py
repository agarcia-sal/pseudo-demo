import math

def sum_squares(lst):
    squared = 0
    index = 0
    while index < len(lst):
        element = lst[index]
        math_ceil_result = math.ceil(element)
        squared += math_ceil_result * math_ceil_result
        index += 1
    return squared