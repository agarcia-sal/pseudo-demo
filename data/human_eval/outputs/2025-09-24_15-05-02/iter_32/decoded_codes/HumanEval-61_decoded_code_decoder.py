def correct_bracketing(string_of_brackets: str) -> bool:
    depth: int = 0
    for bracket_character in string_of_brackets:
        if bracket_character == "(":
            depth += 1
        else:
            depth -= 1
        if depth < 0:
            return False
    return depth == 0