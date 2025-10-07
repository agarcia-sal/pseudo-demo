def is_happy(s) -> bool:
    if len(s) < 3:
        return False
    limit = len(s) - 2
    for i in range(limit):
        if s[i] == s[i+1] or s[i+1] == s[i+2] or s[i] == s[i+2]:
            return False
    return True