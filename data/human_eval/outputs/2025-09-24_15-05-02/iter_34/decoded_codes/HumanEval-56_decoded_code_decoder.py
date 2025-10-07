def correct_bracketing(brackets_string: str) -> bool:
    depth_counter: int = 0
    for bracket_character in brackets_string:
        if bracket_character == "<":
            depth_counter += 1
        else:
            depth_counter -= 1
        if depth_counter < 0:
            return False
    return depth_counter == 0