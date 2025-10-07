def circular_shift(x, shift):
    s = str(x)
    if shift > len(s):
        reversed_s = ''
        index = len(s) - 1
        while index >= 0:
            reversed_s += s[index]
            index -= 1
        return reversed_s
    else:
        length = len(s)
        part1 = ''
        index = length - shift
        while index < length:
            part1 += s[index]
            index += 1
        part2 = ''
        index = 0
        while index < length - shift:
            part2 += s[index]
            index += 1
        return part1 + part2