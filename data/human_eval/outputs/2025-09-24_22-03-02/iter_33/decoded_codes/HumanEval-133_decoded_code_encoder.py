def sum_squares(lst) -> int:
    import math
    squared = 0
    for index in range(len(lst)):
        current_element = lst[index]
        ceiling_value = math.ceil(current_element)
        squared_value = ceiling_value * ceiling_value
        squared += squared_value
    return squared