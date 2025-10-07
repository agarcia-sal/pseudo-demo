from typing import Union

def change_base(integer_number: int, base_number: int) -> str:
    if integer_number == 0:
        return "0"
    result_string = ""
    while integer_number > 0:
        result_string = str(integer_number % base_number) + result_string
        integer_number //= base_number
    return result_string