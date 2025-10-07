def is_happy(s: str) -> bool:
    if len(s) < 3:
        return False
    index = 0
    while index < len(s) - 2:
        if s[index] == s[index + 1] or s[index + 1] == s[index + 2] or s[index] == s[index + 2]:
            return False
        index += 1
    return True