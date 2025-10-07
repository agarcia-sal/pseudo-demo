def correct_bracketing(brackets_string: str) -> bool:
    current_level: int = 0
    for symbol in brackets_string:
        if symbol == "<":
            current_level += 1
        else:
            current_level -= 1
        if current_level < 0:
            return False
    return current_level == 0