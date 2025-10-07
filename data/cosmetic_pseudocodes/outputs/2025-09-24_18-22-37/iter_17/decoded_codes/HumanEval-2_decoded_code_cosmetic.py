from math import floor

def truncate_number(pivot: float) -> float:
    residue: float = pivot - floor(pivot)
    return residue