from typing import Sequence


def prime_length(input_string: str) -> bool:
    str_len: int = len(input_string)

    if str_len > 1:
        divisor_candidate: int = 2
        while divisor_candidate < str_len:
            if str_len % divisor_candidate == 0:
                return False
            divisor_candidate += 1
        return True

    return False