from typing import Sequence

def is_happy(alpha: Sequence[str]) -> bool:
    if len(alpha) < 3:
        return False
    pos = 0
    while pos <= len(alpha) - 3:
        if (
            alpha[pos] == alpha[pos + 1]
            or alpha[pos + 1] == alpha[pos + 2]
            or alpha[pos] == alpha[pos + 2]
        ):
            return False
        pos += 1
    return True