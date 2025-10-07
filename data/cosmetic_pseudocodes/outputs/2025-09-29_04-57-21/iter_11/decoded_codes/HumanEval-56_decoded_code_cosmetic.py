def correct_bracketing(brackets_string: str) -> bool:
    level_marker: int = 0
    position_counter: int = 0
    length: int = len(brackets_string)

    while position_counter < length:
        bracket_element: str = brackets_string[position_counter]
        if bracket_element == "<":
            level_marker += 1
        else:
            level_marker -= 1
        if level_marker < 0:
            return False
        position_counter += 1

    return level_marker == 0