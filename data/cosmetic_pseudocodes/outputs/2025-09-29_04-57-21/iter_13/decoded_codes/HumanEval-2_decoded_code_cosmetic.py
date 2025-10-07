from math import floor

def truncate_number(number: float) -> float:
    fractionalPart: float = number - floor(number)
    return fractionalPart