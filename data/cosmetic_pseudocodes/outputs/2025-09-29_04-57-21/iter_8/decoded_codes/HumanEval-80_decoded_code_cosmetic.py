def is_happy(string_input: str) -> bool:
    if len(string_input) < 3:
        return False

    for position in range(len(string_input) - 2):
        first_char = string_input[position]
        second_char = string_input[position + 1]
        third_char = string_input[position + 2]

        if not (first_char != second_char and second_char != third_char and first_char != third_char):
            return False

    return True