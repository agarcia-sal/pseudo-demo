from typing import Literal

def correct_bracketing(string_of_brackets: str) -> bool:
    depth: int = 0
    for bracket in string_of_brackets:
        if bracket == "<":
            depth += 1
        else:
            depth -= 1
        if depth < 0:
            return False
    return depth == 0