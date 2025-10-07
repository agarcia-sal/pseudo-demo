def circular_shift(x, shift):
    s = str(x)
    if shift > len(s):
        return s[::-1]
    prefix = s[:len(s) - shift]
    suffix = s[len(s) - shift:]
    return suffix + prefix