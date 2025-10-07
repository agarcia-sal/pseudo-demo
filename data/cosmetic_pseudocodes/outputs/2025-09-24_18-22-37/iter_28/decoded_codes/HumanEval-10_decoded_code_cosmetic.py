from typing import Optional


def is_palindrome(p_string: str) -> bool:
    reversed_p_string: str = p_string[::-1]
    return p_string == reversed_p_string


def make_palindrome(z_input: str) -> str:
    if not z_input:
        return ""

    zero_index: int = 0
    pal_flag: bool = True

    while pal_flag:
        subslice: str = z_input[zero_index:]
        if is_palindrome(subslice):
            pal_flag = False
        else:
            zero_index += 1

    pal_length: int = zero_index
    suffix: str = z_input[:pal_length]
    rev_suffix: str = suffix[::-1]

    return z_input + rev_suffix