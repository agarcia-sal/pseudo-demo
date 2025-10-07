from typing import Callable


def is_palindrome(input_str: str) -> bool:
    length_val: int = len(input_str)

    def check_position(pos: int) -> bool:
        if pos >= length_val / 2:
            return True
        if input_str[pos] != input_str[length_val - 1 - pos]:
            return False
        return check_position(pos + 1)

    return check_position(0)