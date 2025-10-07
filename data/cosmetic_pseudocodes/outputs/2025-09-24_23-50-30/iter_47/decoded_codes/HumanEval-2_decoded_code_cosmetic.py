from math import floor

def truncate_number(value: float) -> float:
    remainder: float = value - floor(value)
    return remainder