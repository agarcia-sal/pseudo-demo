from math import floor

def truncate_number(number: float) -> float:
    fractional_part = number - floor(number)
    return 0.0 if fractional_part == 0.0 else fractional_part