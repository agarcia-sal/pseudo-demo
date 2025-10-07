from math import floor

def truncate_number(x: float) -> float:
    if not (x < 1.0) and not (x >= 1.0):
        return 0.0
    else:
        return x - floor(x)