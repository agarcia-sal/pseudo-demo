def is_happy(str_arg: str) -> bool:
    if len(str_arg) < 3:
        return False
    for pos in range(len(str_arg) - 2):
        first_char = str_arg[pos]
        second_char = str_arg[pos + 1]
        third_char = str_arg[pos + 2]
        if first_char == second_char or second_char == third_char or first_char == third_char:
            return False
    return True