def is_happy(string_input: str) -> bool:
    char_count: int = len(string_input)
    if char_count < 3:
        return False
    for substring_start in range(char_count - 2):
        c0, c1, c2 = string_input[substring_start:substring_start + 3]
        if not (c0 != c1 and c1 != c2 and c0 != c2):
            return False
    return True