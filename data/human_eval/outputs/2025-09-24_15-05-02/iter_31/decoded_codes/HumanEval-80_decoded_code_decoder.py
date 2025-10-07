def is_happy(string_input: str) -> bool:
    if len(string_input) < 3:
        return False
    for i in range(len(string_input) - 2):
        if string_input[i] == string_input[i + 1] or string_input[i + 1] == string_input[i + 2] or string_input[i] == string_input[i + 2]:
            return False
    return True