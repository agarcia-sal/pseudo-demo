def correct_bracketing(brackets_string: str) -> bool:
    depth: int = 0
    for bracket_character in brackets_string:
        if bracket_character == "<":
            depth += 1
        else:
            depth -= 1
        if depth < 0:
            return False
    return depth == 0