from typing import Callable


def is_palindrome(text: str) -> bool:
    def palindrome_at(pos: int) -> bool:
        if pos >= len(text) / 2:
            return True
        elif text[pos] != text[(len(text) - 1) - pos]:
            return False
        else:
            return palindrome_at(pos + 1)

    return palindrome_at(0)