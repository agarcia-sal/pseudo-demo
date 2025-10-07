from math import floor

def truncate_number(x: float) -> float:
    y: float = x - floor(x)  # fractional part of x
    return y