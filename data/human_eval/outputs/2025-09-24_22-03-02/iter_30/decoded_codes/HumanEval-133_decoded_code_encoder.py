import math

def sum_squares(lst):
    squared = 0
    for index in range(len(lst)):
        element = lst[index]
        ceiling_value = math.ceil(element)
        square_value = ceiling_value * ceiling_value
        squared += square_value
    return squared