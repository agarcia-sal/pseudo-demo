from math import floor

def truncate_number(number: float) -> float:
    remainder_value: float = number - floor(number)  # fractional part of the number
    return remainder_value