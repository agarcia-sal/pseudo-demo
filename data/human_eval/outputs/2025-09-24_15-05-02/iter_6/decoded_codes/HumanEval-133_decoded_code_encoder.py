import math

def sum_squares(list_of_numbers):
    squared = 0
    for number in list_of_numbers:
        rounded_number = math.ceil(number)
        squared += rounded_number ** 2
    return squared