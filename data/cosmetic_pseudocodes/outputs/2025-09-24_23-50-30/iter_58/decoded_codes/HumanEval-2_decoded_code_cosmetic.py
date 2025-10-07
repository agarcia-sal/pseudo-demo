from math import floor

def truncate_number(w: float) -> float:
    x: float = w - floor(w)
    return x