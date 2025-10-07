import math

def sum_squares(lst):
    squared = 0
    for number in lst:
        rounded_number = math.ceil(number)
        squared += rounded_number * rounded_number
    return squared