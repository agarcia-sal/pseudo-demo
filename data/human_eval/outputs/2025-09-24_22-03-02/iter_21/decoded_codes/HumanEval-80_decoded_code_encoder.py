def is_happy(s):
    if len(s) < 3:
        return False
    i = 0
    while i <= len(s) - 3:
        if s[i] == s[i+1] or s[i+1] == s[i+2] or s[i] == s[i+2]:
            return False
        i += 1
    return True