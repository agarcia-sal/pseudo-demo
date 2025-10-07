from math import floor

def truncate_number(value: float) -> float:
    if value - floor(value) != 0.0:
        return value - floor(value)
    else:
        return 0.0