from math import floor

def truncate_number(number: float) -> float:
    fractional_part = number - floor(number)
    return fractional_part