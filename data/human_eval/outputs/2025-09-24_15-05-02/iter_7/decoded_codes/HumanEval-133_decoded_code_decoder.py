from math import ceil

def sum_squares(list_of_numbers):
    squared_sum = 0
    for number in list_of_numbers:
        ceiling_value = ceil(number)
        squared_sum += ceiling_value * ceiling_value
    return squared_sum