from math import floor

def truncate_number(number: float) -> float:
    fractionalPart = number - floor(number)
    return fractionalPart