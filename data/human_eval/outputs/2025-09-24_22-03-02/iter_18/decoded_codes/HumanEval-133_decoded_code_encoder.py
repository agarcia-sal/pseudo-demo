import math

def sum_squares(lst) -> int:
    squared = 0
    for index in range(len(lst)):
        element = lst[index]
        math_ceil_result = math.ceil(element)
        squared_value = math_ceil_result * math_ceil_result
        squared += squared_value
    return squared