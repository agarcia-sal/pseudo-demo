from math import floor

def truncate_number(number: float) -> float:
    fraction_part: float = number - floor(number)
    return fraction_part