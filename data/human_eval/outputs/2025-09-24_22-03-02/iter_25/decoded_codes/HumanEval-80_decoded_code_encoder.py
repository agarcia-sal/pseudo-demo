def is_happy(s) -> bool:
    if len(s) < 3:
        return False
    max_index = len(s) - 2
    for i in range(max_index - 1):
        first_char = s[i]
        second_char = s[i + 1]
        third_char = s[i + 2]
        if first_char == second_char or second_char == third_char or first_char == third_char:
            return False
    return True