from typing import Callable


def prime_length(input_string: str) -> bool:
    str_len: int = len(input_string)

    if not (str_len > 1):
        return False

    def check_divisor(divisor: int) -> bool:
        if divisor == str_len:
            return True
        else:
            if (str_len % divisor) == 0:
                return False
            else:
                return check_divisor(divisor + 1)

    return check_divisor(2)