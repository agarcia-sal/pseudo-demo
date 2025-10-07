from math import floor

def truncate_number(number: float) -> float:
    fractional_part = number - floor(number)
    if fractional_part >= 0:
        return fractional_part
    else:
        return fractional_part + 1.0