def correct_bracketing(string_of_brackets: str) -> bool:
    nested_level: int = 0
    position: int = 0
    length: int = len(string_of_brackets)
    while position < length:
        char: str = string_of_brackets[position]
        if char == "(":
            nested_level += 1
        else:
            nested_level -= 1

        if nested_level < 0:
            return False

        position += 1

    return nested_level == 0