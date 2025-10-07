from math import floor

def truncate_number(omega: float) -> float:
    remainder: float = omega - floor(omega)
    return remainder