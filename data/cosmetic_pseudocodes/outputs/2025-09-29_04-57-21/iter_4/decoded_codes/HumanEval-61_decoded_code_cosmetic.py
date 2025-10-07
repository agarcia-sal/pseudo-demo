def correct_bracketing(string_of_brackets: str) -> bool:
    nesting_level: int = 0
    position: int = 0
    length: int = len(string_of_brackets)
    while position < length:
        current_char: str = string_of_brackets[position]
        if current_char == "(":
            nesting_level += 1
        else:
            nesting_level -= 1
        if nesting_level < 0:
            return False
        position += 1
    return nesting_level == 0