from math import floor

def truncate_number(n: float) -> float:
    remainder: float = n - floor(n)
    return remainder