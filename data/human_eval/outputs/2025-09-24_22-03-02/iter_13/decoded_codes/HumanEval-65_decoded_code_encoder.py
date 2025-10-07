def circular_shift(x, shift) -> str:
    s = str(x)
    if shift > len(s):
        return s[::-1]
    else:
        return s[-shift:] + s[:-shift]