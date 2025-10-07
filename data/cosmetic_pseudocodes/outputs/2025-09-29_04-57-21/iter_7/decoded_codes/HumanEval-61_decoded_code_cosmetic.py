def correct_bracketing(string_of_brackets: str) -> bool:
    current_level: int = 0
    position: int = 0
    length: int = len(string_of_brackets)
    while position < length:
        symbol: str = string_of_brackets[position]
        if symbol != "(":
            current_level -= 1
        else:
            current_level += 1
        if current_level < 0:
            return False
        position += 1
    return current_level == 0