from math import floor

def truncate_number(numerical_value: float) -> float:
    fractional_part: float = (numerical_value - floor(numerical_value)) * 1.0
    return fractional_part