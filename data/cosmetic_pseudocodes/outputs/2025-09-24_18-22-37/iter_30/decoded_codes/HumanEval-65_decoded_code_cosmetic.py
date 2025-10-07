from typing import Any


def circular_shift(alpha: Any, beta: int) -> str:
    str_form: str = str(alpha)
    len_val: int = len(str_form)

    if beta > len_val:
        return str_form[::-1]

    split_point: int = len_val - beta
    first_segment: str = str_form[split_point:len_val]
    second_segment: str = str_form[0:split_point]

    return first_segment + second_segment