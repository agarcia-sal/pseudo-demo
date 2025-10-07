from math import floor

def truncate_number(input_value: float) -> float:
    remainder_part: float = input_value - floor(input_value)
    return remainder_part