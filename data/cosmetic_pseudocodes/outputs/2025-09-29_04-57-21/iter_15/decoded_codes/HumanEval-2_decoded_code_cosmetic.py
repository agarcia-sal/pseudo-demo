from math import floor

def truncate_number(number: float) -> float:
    decimal_part: float = number - floor(number)
    return decimal_part