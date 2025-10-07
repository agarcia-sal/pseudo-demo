def is_happy(s: str) -> bool:
    if len(s) < 3:
        return False
    for i in range(len(s) - 2):
        if not (s[i] != s[i+1] != s[i+2] != s[i]):
            return False
    return True