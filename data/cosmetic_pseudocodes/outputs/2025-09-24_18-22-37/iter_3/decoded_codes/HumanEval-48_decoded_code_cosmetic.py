from typing import Callable


def is_palindrome(text: str) -> bool:
    def helper(pos: int) -> bool:
        if pos >= len(text) / 2:
            return True
        elif text[pos] != text[len(text) - pos - 1]:
            return False
        else:
            return helper(pos + 1)

    return helper(0)