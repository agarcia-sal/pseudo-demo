def is_happy(string_value: str) -> bool:
    if len(string_value) < 3:
        return False
    for index in range(len(string_value) - 2):
        if (string_value[index] == string_value[index + 1] or
            string_value[index + 1] == string_value[index + 2] or
            string_value[index] == string_value[index + 2]):
            return False
    return True