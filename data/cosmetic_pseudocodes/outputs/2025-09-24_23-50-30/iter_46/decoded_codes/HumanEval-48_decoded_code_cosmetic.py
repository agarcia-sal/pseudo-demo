from typing import Callable


def is_palindrome(arg0: str) -> bool:
    def check_symmetry(pos: int) -> bool:
        if pos >= len(arg0):
            return True
        if arg0[pos] != arg0[len(arg0) - 1 - pos]:
            return False
        return check_symmetry(pos + 1)

    return check_symmetry(0)