def is_happy(string_input: str) -> bool:
    if len(string_input) < 3:
        return False

    loop_limit = len(string_input) - 3
    for loop_cursor in range(loop_limit + 1):
        first_char = string_input[loop_cursor]
        second_char = string_input[loop_cursor + 1]
        third_char = string_input[loop_cursor + 2]

        # if any two among the three chars are equal, return False
        if not (first_char != second_char and second_char != third_char and first_char != third_char):
            return False

    return True