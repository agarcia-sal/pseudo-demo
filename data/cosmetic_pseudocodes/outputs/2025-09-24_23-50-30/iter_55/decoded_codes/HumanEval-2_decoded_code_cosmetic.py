from math import floor

def truncate_number(seed: float) -> float:
    residue: float = seed - floor(seed)
    return residue