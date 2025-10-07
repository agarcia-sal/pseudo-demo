from typing import Union

def correct_bracketing(bracket_string: str) -> bool:
    bracket_depth: int = 0
    for bracket_character in bracket_string:
        if bracket_character == "<":
            bracket_depth += 1
        else:
            bracket_depth -= 1
        if bracket_depth < 0:
            return False
    return bracket_depth == 0