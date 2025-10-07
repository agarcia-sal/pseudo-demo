def circular_shift(x, shift):
    s = str(x)
    length = len(s)
    if shift > length:
        return s[::-1]
    else:
        return s[length - shift:] + s[:length - shift]