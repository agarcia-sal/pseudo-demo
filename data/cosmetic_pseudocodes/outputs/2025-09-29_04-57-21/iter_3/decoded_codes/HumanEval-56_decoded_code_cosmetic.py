def correct_bracketing(brackets_string: str) -> bool:
    nesting_level = 0
    for current_char in brackets_string:
        if current_char != "<":
            nesting_level -= 1
        else:
            nesting_level += 1
        if nesting_level < 0:
            return False
    return nesting_level == 0