from typing import Union

def circular_shift(integer_x: int, integer_shift: int) -> str:
    str_form: str = str(integer_x)
    if len(str_form) < integer_shift:
        return str_form[::-1]
    pivot: int = len(str_form) - integer_shift
    suffix: str = str_form[pivot:]
    prefix: str = str_form[:pivot]
    return suffix + prefix