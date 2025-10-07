from math import floor

def truncate_number(flux: float) -> float:
    flicker: float = flux - floor(flux)
    return flicker