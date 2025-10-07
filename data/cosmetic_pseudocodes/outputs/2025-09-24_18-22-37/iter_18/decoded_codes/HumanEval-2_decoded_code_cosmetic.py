from math import floor

def truncate_number(value: float) -> float:
    remainder_value: float = value - floor(value)
    return remainder_value