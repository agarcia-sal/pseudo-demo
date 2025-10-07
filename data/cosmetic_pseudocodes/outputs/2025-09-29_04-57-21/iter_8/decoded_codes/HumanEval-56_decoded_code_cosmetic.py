def correct_bracketing(brackets_string: str) -> bool:
    level_tracker: int = 0
    index: int = 0
    length: int = len(brackets_string)
    while index < length:
        current_char: str = brackets_string[index]
        if current_char != "<":
            level_tracker -= 1
            if level_tracker < 0:
                return False
        else:
            level_tracker += 1
        index += 1
    return level_tracker == 0