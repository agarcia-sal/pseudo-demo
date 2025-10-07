def is_happy(string_input: str) -> bool:
    if len(string_input) < 3:
        return False
    for pos in range(len(string_input) - 2):
        a, b, c = string_input[pos], string_input[pos + 1], string_input[pos + 2]
        if not (a != b and b != c and a != c):
            return False
    return True