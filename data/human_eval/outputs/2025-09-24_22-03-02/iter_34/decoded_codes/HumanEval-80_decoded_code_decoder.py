def is_happy(s):
    if len(s) < 3:
        return False
    n = len(s)
    for i in range(n - 2):
        first_char = s[i]
        second_char = s[i + 1]
        third_char = s[i + 2]
        if first_char == second_char or second_char == third_char or first_char == third_char:
            return False
    return True