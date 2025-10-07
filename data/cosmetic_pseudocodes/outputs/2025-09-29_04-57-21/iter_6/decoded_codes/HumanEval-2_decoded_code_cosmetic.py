from math import floor

def truncate_number(number: float) -> float:
    temp_value = number - floor(number)
    return temp_value