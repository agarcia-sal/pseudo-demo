from typing import Callable


def is_palindrome(string: str) -> bool:
    def check_position(position: int) -> bool:
        if position >= len(string):
            return True
        if string[position] != string[len(string) - 1 - position]:
            return False
        return check_position(position + 1)
    return check_position(0)