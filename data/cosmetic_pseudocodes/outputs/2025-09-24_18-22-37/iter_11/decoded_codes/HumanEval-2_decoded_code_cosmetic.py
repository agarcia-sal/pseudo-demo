from math import floor

def truncate_number(value: float) -> float:
    fractional_part: float = value - floor(value)
    return fractional_part