from math import floor

def truncate_number(value: float) -> float:
    remainder_part: float = value - floor(value)
    return remainder_part