def circular_shift(x: int, shift: int) -> str:
    s = str(x)
    if shift > len(s):
        return s[::-1]
    else:
        prefix = s[:len(s) - shift]
        suffix = s[len(s) - shift:]
        return suffix + prefix