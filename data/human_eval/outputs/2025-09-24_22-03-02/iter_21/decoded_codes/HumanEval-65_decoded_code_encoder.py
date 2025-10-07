def circular_shift(x, shift):
    s = str(x)
    if shift > len(s):
        return s[::-1]
    else:
        first_part = s[len(s)-shift:len(s)]
        second_part = s[0:len(s)-shift]
        return first_part + second_part