from math import floor

def truncate_number(x: float) -> float:
    r: float = x - floor(x)
    return r