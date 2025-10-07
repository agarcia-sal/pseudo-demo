from math import floor

def truncate_number(value: float) -> float:
    remainderPart: float = value - floor(value)
    return remainderPart