def is_happy(s) -> bool:
    length = len(s)
    if length < 3:
        return False
    limit = length - 2
    i = 0
    while i < limit:
        first_char = s[i]
        second_char = s[i + 1]
        third_char = s[i + 2]
        if first_char == second_char or second_char == third_char or first_char == third_char:
            return False
        i += 1
    return True