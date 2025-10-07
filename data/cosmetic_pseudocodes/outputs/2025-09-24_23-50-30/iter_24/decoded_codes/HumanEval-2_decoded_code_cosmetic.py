from math import floor

def truncate_number(alpha: float) -> float:
    beta: float = alpha - floor(alpha)
    return beta