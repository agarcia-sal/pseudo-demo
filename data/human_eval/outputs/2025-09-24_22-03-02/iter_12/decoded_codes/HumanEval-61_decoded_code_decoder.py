from typing import List

def correct_bracketing(BRACKETS: List[str]) -> bool:
    DEPTH = 0
    for B in BRACKETS:
        if B == "(":
            DEPTH += 1
        else:
            DEPTH -= 1
        if DEPTH < 0:
            return False
    return DEPTH == 0