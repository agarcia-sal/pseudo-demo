def is_happy(input_str: str) -> bool:
    len_val = len(input_str)
    if len_val < 3:
        return False
    pos = 0
    while pos <= len_val - 3:
        first_char = input_str[pos]
        second_char = input_str[pos + 1]
        third_char = input_str[pos + 2]
        if first_char == second_char:
            return False
        if second_char == third_char:
            return False
        if first_char == third_char:
            return False
        pos += 1
    return True