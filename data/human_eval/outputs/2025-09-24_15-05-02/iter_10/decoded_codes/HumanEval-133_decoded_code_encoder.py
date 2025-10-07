import math

def sum_squares(list_of_numbers):
    squared = 0
    for number in list_of_numbers:
        ceiling_value = math.ceil(number)
        squared += ceiling_value * ceiling_value
    return squared