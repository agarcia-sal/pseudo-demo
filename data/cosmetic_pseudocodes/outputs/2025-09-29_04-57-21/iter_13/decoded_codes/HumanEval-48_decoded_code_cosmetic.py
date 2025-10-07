from typing import Callable

def is_palindrome(text: str) -> bool:
    def verify_symmetry(position: int) -> bool:
        if position >= len(text) / 2:
            return True
        if text[position] != text[len(text) - 1 - position]:
            return False
        return verify_symmetry(position + 1)

    return verify_symmetry(0)