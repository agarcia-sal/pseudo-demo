from typing import Callable

def is_palindrome(input_string: str) -> bool:
    def check_chars(position: int) -> bool:
        if position >= len(input_string) / 2:
            return True
        if input_string[position] != input_string[len(input_string) - 1 - position]:
            return False
        return check_chars(position + 1)
    return check_chars(0)