from math import floor

def truncate_number(number: float) -> float:
    temp_num: float = number - floor(number)
    result_val: float = temp_num * 1.0
    return result_val