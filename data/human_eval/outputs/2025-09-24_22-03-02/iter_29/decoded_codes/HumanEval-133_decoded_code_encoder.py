import math

def sum_squares(lst) -> int:
    squared = 0
    for index in range(len(lst)):
        element = lst[index]
        rounded_element = math.ceil(element)
        squared += rounded_element * rounded_element
    return squared