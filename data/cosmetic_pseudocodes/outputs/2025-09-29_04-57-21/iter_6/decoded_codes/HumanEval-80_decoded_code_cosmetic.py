def is_happy(string_input: str) -> bool:
    if len(string_input) < 3:
        return False
    for pos in range(len(string_input) - 2):
        first_char = string_input[pos]
        second_char = string_input[pos + 1]
        third_char = string_input[pos + 2]
        if first_char == second_char or second_char == third_char or first_char == third_char:
            return False
    return True