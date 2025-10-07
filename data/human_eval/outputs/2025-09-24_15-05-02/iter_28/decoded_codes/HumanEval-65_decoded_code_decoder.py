def circular_shift(x: int, shift: int) -> str:
    s = str(x)
    length = len(s)
    if shift > length:
        return s[::-1]
    return s[length - shift :] + s[: length - shift]