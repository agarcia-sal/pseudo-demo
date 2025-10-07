def circular_shift(x, shift):
    s = str(x)
    if shift > len(s):
        return s[::-1]
    else:
        part1 = s[-shift:]
        part2 = s[:-shift]
        return part1 + part2