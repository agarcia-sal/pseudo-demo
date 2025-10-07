from typing import Callable

def is_palindrome(text: str) -> bool:
    def verifySymmetry(position: int, limit: int) -> bool:
        if position >= limit:
            return True
        if text[position] != text[(limit - 1) - position]:
            return False
        return verifySymmetry(position + 1, limit)

    return verifySymmetry(0, len(text))