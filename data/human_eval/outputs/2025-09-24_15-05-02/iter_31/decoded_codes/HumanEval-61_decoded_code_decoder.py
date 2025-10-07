def correct_bracketing(string_of_brackets: str) -> bool:
    depth_counter = 0
    for bracket_character in string_of_brackets:
        if bracket_character == "(":
            depth_counter += 1
        else:
            depth_counter -= 1
        if depth_counter < 0:
            return False
    return depth_counter == 0