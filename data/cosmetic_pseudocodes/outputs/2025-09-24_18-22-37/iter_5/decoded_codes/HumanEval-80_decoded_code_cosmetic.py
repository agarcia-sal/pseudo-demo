def is_happy(input_str: str) -> bool:
    if len(input_str) < 3:
        return False

    limit = len(input_str) - 3
    for counter in range(limit + 1):
        first_char = input_str[counter]
        second_char = input_str[counter + 1]
        third_char = input_str[counter + 2]

        if first_char == second_char or second_char == third_char or first_char == third_char:
            return False

    return True