def is_happy(string_input: str) -> bool:
    if len(string_input) < 3:
        return False
    for i in range(len(string_input) - 2):
        a, b, c = string_input[i], string_input[i + 1], string_input[i + 2]
        if not (a != b and b != c and a != c):
            return False
    return True