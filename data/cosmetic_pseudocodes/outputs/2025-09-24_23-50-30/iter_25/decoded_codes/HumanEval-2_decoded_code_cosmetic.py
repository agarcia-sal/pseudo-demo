from math import floor

def truncate_number(value: float) -> float:
    result: float = value - floor(value)
    return result