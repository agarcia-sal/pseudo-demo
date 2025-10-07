def is_happy(string_input: str) -> bool:
    num_chars: int = len(string_input)
    if num_chars < 3:
        return False

    pos: int = 0
    while pos <= num_chars - 3:
        first_char: str = string_input[pos]
        second_char: str = string_input[pos + 1]
        third_char: str = string_input[pos + 2]

        if first_char == second_char or second_char == third_char or first_char == third_char:
            return False

        pos += 1

    return True