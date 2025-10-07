from typing import Optional


def circular_shift(integer_x: int, integer_shift: int) -> str:
    str_form: str = str(integer_x)
    len_str: int = len(str_form)

    if not (integer_shift <= len_str):
        # Reverse the string manually
        rev_str: str = ""
        idx: int = len_str - 1
        while idx >= 0:
            rev_str += str_form[idx]
            idx -= 1
        return rev_str

    split_point: int = len_str - integer_shift
    part_one: str = ""
    part_two: str = ""

    i: int = split_point
    while i < len_str:
        part_one += str_form[i]
        i += 1

    j: int = 0
    while j < split_point:
        part_two += str_form[j]
        j += 1

    return part_one + part_two