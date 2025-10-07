def sum_squares(list_of_numbers):
    import math
    squared = 0
    for element in list_of_numbers:
        squared += (math.ceil(element)) ** 2
    return squared