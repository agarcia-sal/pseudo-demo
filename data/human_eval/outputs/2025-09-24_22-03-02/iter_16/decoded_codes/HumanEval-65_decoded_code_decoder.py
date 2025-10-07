def circular_shift(x: int, shift: int) -> str:
    s = str(x)
    if shift > len(s):
        return s[::-1]
    else:
        first_part = s[len(s)-shift:]
        second_part = s[:len(s)-shift]
        return first_part + second_part