from typing import AnyStr

def prime_length(input_string: AnyStr) -> bool:
    str_len: int = len(input_string)
    if str_len <= 1:
        return False
    for candidate_divisor in range(2, str_len):
        if str_len % candidate_divisor == 0:
            return False
    return True