from typing import List

def correct_bracketing(BRACKETS: List[str]) -> bool:
    depth = 0
    for b in BRACKETS:
        if b == "<":
            depth += 1
        else:
            depth -= 1
        if depth < 0:
            return False
    return depth == 0