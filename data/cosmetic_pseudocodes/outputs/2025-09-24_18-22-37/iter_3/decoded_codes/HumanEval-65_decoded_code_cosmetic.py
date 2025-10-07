from typing import Optional


def circular_shift(integer_x: int, integer_shift: int) -> str:
    str_form: str = ""
    idx: int = 0
    str_x = str(integer_x)
    length = len(str_x)
    # Build the string representation manually
    while idx < length:
        str_form += str_x[idx]
        idx += 1

    if not (integer_shift <= len(str_form)):
        reversed_str: str = ""
        rev_idx: int = len(str_form) - 1
        # Build reversed string manually
        while rev_idx >= 0:
            reversed_str += str_form[rev_idx]
            rev_idx -= 1
        return reversed_str
    else:
        n: int = len(str_form)
        first_part: str = ""
        second_part: str = ""
        i: int = n - integer_shift
        while i < n:
            first_part += str_form[i]
            i += 1
        j: int = 0
        while j < n - integer_shift:
            second_part += str_form[j]
            j += 1
        return first_part + second_part