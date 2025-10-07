def correct_bracketing(string_of_brackets: str) -> bool:
    depth_counter: int = 0
    index: int = 0
    length: int = len(string_of_brackets)
    while index < length:
        current_char: str = string_of_brackets[index]
        if current_char != '(':
            depth_counter -= 1
        else:
            depth_counter += 1
        if depth_counter < 0:
            return False
        index += 1
    return depth_counter == 0