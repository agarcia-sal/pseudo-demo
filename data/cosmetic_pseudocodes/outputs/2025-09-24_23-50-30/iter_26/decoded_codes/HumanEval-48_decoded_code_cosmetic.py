from typing import Callable

def is_palindrome(inputString: str) -> bool:
    def check_chars(position: int) -> bool:
        if position >= len(inputString) / 2:
            return True
        if inputString[position] != inputString[len(inputString) - 1 - position]:
            return False
        return check_chars(position + 1)
    return check_chars(0)