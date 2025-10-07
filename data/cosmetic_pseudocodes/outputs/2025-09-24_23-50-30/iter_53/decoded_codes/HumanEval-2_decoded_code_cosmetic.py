from math import floor

def truncate_number(value: float) -> float:
    temp: float = value
    frac: float = temp - floor(temp)
    return frac