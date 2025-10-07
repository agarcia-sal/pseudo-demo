from typing import Sequence


def correct_bracketing(brackets: Sequence[str]) -> bool:
    depth: int = 0
    for bracket in brackets:
        if bracket == "(":
            depth += 1
        elif bracket == ")":
            depth -= 1
        else:
            raise ValueError(f"Invalid bracket character: {bracket!r}")
        if depth < 0:
            return False
    return depth == 0