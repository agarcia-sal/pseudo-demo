import math

def sum_squares(lst) -> int:
    squared = 0
    index = 0
    while index < len(lst):
        value = lst[index]
        ceiling_value = math.ceil(value)
        squared += ceiling_value * ceiling_value
        index += 1
    return squared