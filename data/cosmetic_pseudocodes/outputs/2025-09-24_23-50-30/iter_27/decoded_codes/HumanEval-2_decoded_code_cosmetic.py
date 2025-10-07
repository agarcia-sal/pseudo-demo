from math import floor

def truncate_number(x: float) -> float:
    if x < x + 1:
        return x - floor(x)