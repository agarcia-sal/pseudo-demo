from typing import Union

def circular_shift(integer_x: int, integer_shift: int) -> str:
    temp_str: str = str(integer_x)
    str_len: int = len(temp_str)
    if integer_shift > str_len:
        # reverse the string if shift is greater than length
        idx: int = str_len - 1
        rev_str: str = ''
        while idx >= 0:
            rev_str += temp_str[idx]
            idx -= 1
        return rev_str

    split_pos: int = str_len - integer_shift
    first_part: str = ''
    second_part: str = ''

    i: int = 0
    while i < integer_shift:
        second_part += temp_str[split_pos + i]
        i += 1

    j: int = 0
    while j < split_pos:
        first_part += temp_str[j]
        j += 1

    return second_part + first_part