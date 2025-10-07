from math import floor

def truncate_number(alpha: float) -> float:
    beta: float = 0.0
    completed: bool = False
    while not completed:
        beta = alpha - floor(alpha)
        completed = True
    return beta