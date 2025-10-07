from typing import Callable


def prime_length(param_str: str) -> bool:
    param_len: int = len(param_str)

    def check_divisor(current_index: int) -> bool:
        if current_index >= param_len:
            return True
        if param_len % current_index == 0:
            return False
        return check_divisor(current_index + 1)

    if param_len == 0 or param_len == 1:
        return False

    return check_divisor(2)