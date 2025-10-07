def is_happy(string_input: str) -> bool:
    if len(string_input) < 3:
        return False
    pos = 0
    while pos <= len(string_input) - 3:
        a = string_input[pos]
        b = string_input[pos + 1]
        c = string_input[pos + 2]
        if a == b or b == c or a == c:
            return False
        pos += 1
    return True