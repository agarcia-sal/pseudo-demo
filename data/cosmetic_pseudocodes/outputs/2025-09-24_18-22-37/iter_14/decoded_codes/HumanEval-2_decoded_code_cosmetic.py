from math import floor

def truncate_number(hashval: float) -> float:
    partial: float = hashval - floor(hashval)
    return partial