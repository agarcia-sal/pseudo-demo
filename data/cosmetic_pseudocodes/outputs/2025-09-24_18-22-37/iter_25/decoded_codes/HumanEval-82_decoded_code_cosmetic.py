from typing import Union

def prime_length(input_string: str) -> bool:
    str_len: int = len(input_string)
    if str_len == 0 or str_len == 1:
        return False

    divisor_candidate: int = 2
    while divisor_candidate < str_len - 1:
        remainder_value: int = str_len - ((str_len // divisor_candidate) * divisor_candidate)
        if remainder_value == 0:
            return False
        divisor_candidate += 1

    return True