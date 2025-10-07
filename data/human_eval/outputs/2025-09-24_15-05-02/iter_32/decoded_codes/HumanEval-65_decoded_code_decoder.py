def circular_shift(integer_x: int, integer_shift: int) -> str:
    s: str = str(integer_x)
    if integer_shift > len(s):
        return s[::-1]
    else:
        return s[len(s) - integer_shift :] + s[: len(s) - integer_shift]