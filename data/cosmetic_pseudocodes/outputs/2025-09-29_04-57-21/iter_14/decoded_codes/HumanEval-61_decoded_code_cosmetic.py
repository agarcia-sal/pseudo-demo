def correct_bracketing(string_of_brackets: str) -> bool:
    level: int = 0
    position: int = 0
    length: int = len(string_of_brackets)
    while position < length:
        current_char: str = string_of_brackets[position]
        if current_char != "(":
            level -= 1
        else:
            level += 1
        if level < 0:
            return False
        position += 1
    return level == 0