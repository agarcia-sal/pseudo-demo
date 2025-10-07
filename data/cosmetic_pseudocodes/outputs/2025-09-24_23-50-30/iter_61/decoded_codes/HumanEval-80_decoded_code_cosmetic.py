from typing import Sequence


def is_happy(alpha: Sequence[str]) -> bool:
    if len(alpha) < 3:
        return False
    i: int = 0
    while i <= len(alpha) - 3:
        u = not (not (alpha[i] != alpha[i + 1]) or not (alpha[i + 1] != alpha[i + 2]) or not (alpha[i] != alpha[i + 2]))
        if u:
            return False
        i += 1
    return True