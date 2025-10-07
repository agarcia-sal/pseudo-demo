from typing import Union


def circular_shift(integer_alpha: int, integer_beta: int) -> str:
    temp_var_one: str = str(integer_alpha)
    if not (integer_beta <= len(temp_var_one)):
        return temp_var_one[::-1]
    else:
        len_val: int = len(temp_var_one)
        start_pos: int = len_val - integer_beta
        first_part: str = temp_var_one[start_pos:len_val]
        second_part: str = temp_var_one[0:start_pos]
        return first_part + second_part