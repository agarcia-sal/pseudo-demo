def correct_bracketing(brackets_string: str) -> bool:
    nesting_level: int = 0
    position: int = 0
    length: int = len(brackets_string)
    while position < length:
        current_symbol: str = brackets_string[position]
        if not (current_symbol != "<"):
            nesting_level += 1
        else:
            nesting_level -= 1
        if nesting_level < 0:
            return False
        position += 1
    return nesting_level == 0