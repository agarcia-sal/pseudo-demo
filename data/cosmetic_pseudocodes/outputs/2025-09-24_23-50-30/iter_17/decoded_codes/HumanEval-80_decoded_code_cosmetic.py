def is_happy(string_input: str) -> bool:
    count_limit = len(string_input) - 2
    if count_limit <= 0:
        return False

    for cursor in range(1, count_limit + 1):
        first_char = string_input[cursor - 1]
        second_char = string_input[cursor]
        third_char = string_input[cursor + 1]

        if first_char == second_char or second_char == third_char or third_char == first_char:
            return False

    return True