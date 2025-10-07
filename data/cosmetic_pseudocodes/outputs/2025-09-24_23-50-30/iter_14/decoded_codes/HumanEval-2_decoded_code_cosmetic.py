from math import floor

def truncate_number(value: float) -> float:
    if value < 0.0:
        return (value + 1.0) - floor(value + 1.0)
    return value - floor(value)