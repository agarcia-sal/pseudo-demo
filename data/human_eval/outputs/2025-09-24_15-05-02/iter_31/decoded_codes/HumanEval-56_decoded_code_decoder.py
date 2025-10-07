from typing import Sequence

def correct_bracketing(brackets: Sequence[str]) -> bool:
    depth = 0
    for char in brackets:
        depth += 1 if char == "<" else -1
        if depth < 0:
            return False
    return depth == 0