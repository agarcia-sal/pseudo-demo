def circular_shift(x, shift):
    s = str(x)
    length = len(s)
    if shift > length:
        return s[::-1]  # Reverse the string if shift is greater than length
    else:
        part1 = s[length - shift:]
        part2 = s[:length - shift]
        return part1 + part2