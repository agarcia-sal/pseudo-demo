from math import floor

def truncate_number(value: float) -> float:
    fraction_part: float = value - floor(value)
    return fraction_part