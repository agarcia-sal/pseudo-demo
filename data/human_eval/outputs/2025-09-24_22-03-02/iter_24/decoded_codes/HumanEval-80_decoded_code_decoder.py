def is_happy(s: str) -> bool:
    if len(s) < 3:
        return False
    length = len(s)
    for i in range(length - 2):
        if s[i] == s[i+1] or s[i+1] == s[i+2] or s[i] == s[i+2]:
            return False
    return True