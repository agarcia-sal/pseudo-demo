from math import floor

def truncate_number(number: float) -> float:
    fractional_part: float = number - floor(number)
    return fractional_part