import math

def sum_squares(list_of_numbers):
    squared_sum = 0
    for number in list_of_numbers:
        ceiled_number = math.ceil(number)
        squared_sum += ceiled_number ** 2
    return squared_sum