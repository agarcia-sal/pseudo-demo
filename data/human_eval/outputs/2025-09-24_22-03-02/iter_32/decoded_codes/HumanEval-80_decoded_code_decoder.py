def is_happy(s: str) -> bool:
    if len(s) < 3:
        return False
    n = len(s)
    i = 0
    while i < n - 2:
        first_char = s[i]
        second_char = s[i + 1]
        third_char = s[i + 2]
        if first_char == second_char or second_char == third_char or first_char == third_char:
            return False
        i += 1
    return True