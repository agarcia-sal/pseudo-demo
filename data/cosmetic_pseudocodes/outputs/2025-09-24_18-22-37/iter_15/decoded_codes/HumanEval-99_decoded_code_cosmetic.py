from math import floor, ceil
from typing import Union


def closest_integer(theta: str) -> int:
    dot_count: int = 0
    idx: int = 0
    length_theta: int = len(theta)

    while idx < length_theta:
        if theta[idx] == '.':
            dot_count += 1
        idx += 1

    if dot_count == 1:
        finished: bool = False
        while not finished:
            length_var = len(theta)
            if length_var == 0:
                finished = True
            else:
                last_char = theta[length_var - 1]
                if last_char == '0':
                    theta = theta[:length_var - 1]
                else:
                    finished = True

    float_val: float = float(theta) if theta else 0.0

    len_theta = len(theta)
    last_two_chars: str = ''
    if len_theta >= 2:
        last_two_chars = theta[len_theta - 2] + theta[len_theta - 1]

    final_result: int = 0

    if last_two_chars == '.5':
        if float_val > 0:
            final_result = ceil(float_val)
        else:
            final_result = floor(float_val)
    elif len_theta > 0:
        final_result = round(float_val)
    else:
        final_result = 0

    return final_result