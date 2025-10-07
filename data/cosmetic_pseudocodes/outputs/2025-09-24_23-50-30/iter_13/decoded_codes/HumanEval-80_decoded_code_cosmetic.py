def is_happy(string_input: str) -> bool:
    max_pos: int = len(string_input) - 3
    if max_pos < 0:
        return False

    offset: int = 0
    while offset <= max_pos:
        if (
            string_input[offset] == string_input[offset + 1]
            or string_input[offset + 1] == string_input[offset + 2]
            or string_input[offset] == string_input[offset + 2]
        ):
            return False
        offset += 1

    return True