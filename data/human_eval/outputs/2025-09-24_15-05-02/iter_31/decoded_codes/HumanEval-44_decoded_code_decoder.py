from typing import Union

def change_base(integer_number: int, base_number: int) -> str:
    if base_number <= 1:
        raise ValueError("base_number must be greater than 1")
    if integer_number == 0:
        return "0"
    if integer_number < 0:
        raise ValueError("integer_number must be non-negative")
    result_string = ""
    while integer_number > 0:
        result_string = str(integer_number % base_number) + result_string
        integer_number //= base_number
    return result_string