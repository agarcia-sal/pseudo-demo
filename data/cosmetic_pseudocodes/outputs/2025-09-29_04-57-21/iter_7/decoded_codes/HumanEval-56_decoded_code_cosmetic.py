def correct_bracketing(brackets_string: str) -> bool:
    depth_counter: int = 0
    index: int = 0
    while index < len(brackets_string):
        current_char: str = brackets_string[index]
        if current_char == "<":
            depth_counter += 1
        else:
            depth_counter -= 1
        if depth_counter < 0:
            return False
        index += 1
    return depth_counter == 0