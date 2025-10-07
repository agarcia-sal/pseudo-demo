from typing import Union


def prime_length(input_string: Union[str, bytes]) -> bool:
    str_len: int = len(input_string)
    if str_len <= 1:
        return False
    for divisor in range(2, str_len):
        if str_len % divisor == 0:
            return False
    return True