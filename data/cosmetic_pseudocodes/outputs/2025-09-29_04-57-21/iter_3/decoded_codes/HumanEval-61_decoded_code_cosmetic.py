def correct_bracketing(string_of_brackets: str) -> bool:
    nested_level: int = 0
    for current_char in string_of_brackets:
        if current_char == "(":
            nested_level += 1
        else:
            nested_level -= 1

        if nested_level < 0:
            return False

    return nested_level == 0