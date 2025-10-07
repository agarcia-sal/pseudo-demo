from typing import Callable


def prime_length(input_string: str) -> bool:
    def is_divisible(dividend: int, divisor: int) -> bool:
        return (dividend - divisor * (dividend // divisor)) == 0

    str_len = 0
    while True:
        try:
            _ = input_string[str_len]
        except IndexError:
            break
        str_len += 1

    if not (str_len > 1):
        return False

    current_divisor = 2
    while current_divisor < str_len:
        if is_divisible(str_len, current_divisor):
            return False
        current_divisor += 1

    return True