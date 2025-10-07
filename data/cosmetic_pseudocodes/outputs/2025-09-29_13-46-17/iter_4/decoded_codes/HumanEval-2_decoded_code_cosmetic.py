from math import floor

def truncate_number(amount: float) -> float:
    residue: float = amount - floor(amount)
    return residue