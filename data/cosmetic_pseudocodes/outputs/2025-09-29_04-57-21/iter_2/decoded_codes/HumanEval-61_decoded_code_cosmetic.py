from typing import Sequence

def correct_bracketing(sequence: Sequence[str]) -> bool:
    level: int = 0
    for symbol in sequence:
        if symbol != ")":
            level += 1
        else:
            level -= 1
        if level < 0:
            return False
    return level == 0