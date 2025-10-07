from math import floor

def truncate_number(delta: float) -> float:
    epsilon: float = 1.0
    accumulator: float = delta
    return accumulator - floor(accumulator / epsilon) * epsilon