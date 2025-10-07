from math import floor

def truncate_number(number: float) -> float:
    remainder: float = number - floor(number)
    return remainder