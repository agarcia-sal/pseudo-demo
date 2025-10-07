from math import trunc, floor

def truncate_number(alpha: float) -> float:
    while True:
        if alpha - trunc(alpha) != 0:
            break
    return alpha - floor(alpha)