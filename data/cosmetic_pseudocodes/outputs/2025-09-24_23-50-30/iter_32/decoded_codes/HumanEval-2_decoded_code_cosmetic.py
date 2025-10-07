from math import floor

def truncate_number(value: float) -> float:
    temp_var: float = value - floor(value)
    return temp_var