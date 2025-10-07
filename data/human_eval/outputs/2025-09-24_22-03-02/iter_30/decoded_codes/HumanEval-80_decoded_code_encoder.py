def is_happy(s) -> bool:
    if len(s) < 3:
        return False
    n = len(s)
    i = 0
    while i < n - 2:
        if s[i] == s[i + 1] or s[i + 1] == s[i + 2] or s[i] == s[i + 2]:
            return False
        i += 1
    return True