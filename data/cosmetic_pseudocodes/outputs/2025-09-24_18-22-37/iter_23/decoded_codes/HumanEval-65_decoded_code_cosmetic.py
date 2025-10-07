from typing import Optional


def circular_shift(integer_z: int, integer_h: int) -> str:
    string_val: str = str(integer_z)
    len_val: int = len(string_val)

    if integer_h > len_val:
        inverted_string: str = ""
        idx: int = len_val - 1
        while idx >= 0:
            inverted_string += string_val[idx]
            idx -= 1
        return inverted_string
    else:
        front_part: str = string_val[len_val - integer_h : len_val]
        end_part: str = string_val[0 : len_val - integer_h]
        return front_part + end_part