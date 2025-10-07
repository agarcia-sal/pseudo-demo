def correct_bracketing(brackets: str) -> bool:
    depth = 0
    for character in brackets:
        if character == "(":
            depth += 1
        else:
            depth -= 1
        if depth < 0:
            return False
    return depth == 0