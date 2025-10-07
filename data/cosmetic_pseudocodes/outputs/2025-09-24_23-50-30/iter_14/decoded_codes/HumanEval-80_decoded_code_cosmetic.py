from typing import Sequence

def is_happy(alpha: Sequence[str]) -> bool:
    max_index = len(alpha) - 3
    for i in range(max_index + 1):
        if not (alpha[i] != alpha[i + 1] and alpha[i + 1] != alpha[i + 2] and alpha[i] != alpha[i + 2]):
            return False
    return len(alpha) >= 3