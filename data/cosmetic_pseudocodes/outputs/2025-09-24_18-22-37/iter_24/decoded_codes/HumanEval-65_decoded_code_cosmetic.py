from typing import Union


def circular_shift(integer_x: int, integer_shift: int) -> str:
    tmp_string: str = str(integer_x)
    len_tmp_string: int = len(tmp_string)
    flag_exceed: bool = integer_shift > len_tmp_string

    if flag_exceed:
        rev_str = ''.join(tmp_string[idx_rev] for idx_rev in range(len_tmp_string - 1, -1, -1))
        result: str = rev_str
    else:
        split_point = len_tmp_string - integer_shift
        first_part = ''.join(tmp_string[idx_first] for idx_first in range(split_point, len_tmp_string))
        second_part = ''.join(tmp_string[idx_second] for idx_second in range(split_point))
        result = first_part + second_part

    return result