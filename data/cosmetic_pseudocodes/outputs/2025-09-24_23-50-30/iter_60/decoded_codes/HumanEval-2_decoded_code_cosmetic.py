from math import floor

def truncate_number(xy1: float) -> float:
    if (xy1 - floor(xy1)) == (xy1 % 1.0):
        return xy1 % 1.0