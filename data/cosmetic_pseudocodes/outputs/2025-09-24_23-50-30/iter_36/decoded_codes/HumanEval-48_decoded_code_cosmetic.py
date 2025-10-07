from typing import Callable


def is_palindrome(input_string: str) -> bool:
    def check_characters(position: int, limit: int) -> bool:
        if position >= limit:
            return True
        if input_string[position] != input_string[limit - 1 - position]:
            return False
        return check_characters(position + 1, limit)

    return check_characters(0, len(input_string))