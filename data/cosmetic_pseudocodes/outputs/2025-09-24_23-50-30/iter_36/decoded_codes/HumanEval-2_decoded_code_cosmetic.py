from math import floor

def truncate_number(value: float) -> float:
    remainder: float = value - (value - (value - floor(value)))
    return value - floor(value)