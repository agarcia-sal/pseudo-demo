from math import floor

def truncate_number(value: float) -> float:
    temp: float = value - floor(value)
    return temp