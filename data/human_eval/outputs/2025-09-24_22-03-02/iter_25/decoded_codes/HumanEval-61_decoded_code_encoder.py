def correct_bracketing(brackets: str) -> bool:
    depth = 0
    length_of_brackets = len(brackets)
    index = 0
    while index < length_of_brackets:
        b = brackets[index]
        if b == "(":
            depth += 1
        else:
            depth -= 1
        if depth < 0:
            return False
        index += 1
    return depth == 0