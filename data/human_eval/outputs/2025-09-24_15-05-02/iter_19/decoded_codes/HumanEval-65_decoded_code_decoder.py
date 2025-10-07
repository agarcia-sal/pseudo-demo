def circular_shift(x: int, shift: int) -> str:
    s: str = str(x)
    length: int = len(s)
    if shift > length:
        return s[::-1]
    else:
        return s[length - shift:] + s[:length - shift]