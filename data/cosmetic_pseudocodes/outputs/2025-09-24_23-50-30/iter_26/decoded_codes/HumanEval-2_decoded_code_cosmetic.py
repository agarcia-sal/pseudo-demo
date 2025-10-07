from math import floor

def truncate_number(parameter: float) -> float:
    delta: float = parameter - floor(parameter)
    return delta