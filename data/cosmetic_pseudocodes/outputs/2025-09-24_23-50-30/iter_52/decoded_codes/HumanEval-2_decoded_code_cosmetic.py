from math import floor

def truncate_number(param_alpha: float) -> float:
    temp_beta: float = param_alpha - floor(param_alpha)
    return temp_beta