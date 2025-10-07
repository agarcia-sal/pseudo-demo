from math import floor

def truncate_number(x1: float) -> float:
    x2: float = x1 - floor(x1)
    return x2