import math

def sum_squares(lst):
    squared = 0
    for index in range(len(lst)):
        element = lst[index]
        ceiled_element = math.ceil(element)
        squared += ceiled_element * ceiled_element
    return squared