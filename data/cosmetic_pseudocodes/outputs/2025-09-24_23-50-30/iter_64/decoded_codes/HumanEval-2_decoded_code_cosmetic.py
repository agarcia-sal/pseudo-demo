from math import floor

def truncate_number(val_1: float) -> float:
    residue_2: float = val_1 - floor(val_1)
    return residue_2