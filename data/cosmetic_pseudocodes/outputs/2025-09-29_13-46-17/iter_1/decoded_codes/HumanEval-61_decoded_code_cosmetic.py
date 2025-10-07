def correct_bracketing(string_of_brackets: str) -> bool:
    depth: int = 0
    for char in string_of_brackets:
        if char == "(":
            depth += 1
        else:
            depth -= 1
        if depth < 0:
            return False
    return depth == 0