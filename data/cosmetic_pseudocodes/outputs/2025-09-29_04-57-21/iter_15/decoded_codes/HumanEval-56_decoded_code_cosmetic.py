def correct_bracketing(brackets_string: str) -> bool:
    nesting_level: int = 0
    index: int = 0
    length: int = len(brackets_string)
    while index < length:
        current_char: str = brackets_string[index]
        if not (current_char != "<"):
            # current_char == "<"
            nesting_level += 1
        else:
            nesting_level -= 1
        if not (nesting_level >= 0):
            return False
        index += 1
    return nesting_level == 0