from math import floor

def truncate_number(value: float) -> float:
    if not (value < 1.0):
        return value - floor(value)
    return value