def circular_shift(x, shift):
    s = str(x)
    if shift > len(s):
        reversed_string = ''
        index = len(s) - 1
        while index >= 0:
            reversed_string += s[index]
            index -= 1
        return reversed_string
    else:
        length_s = len(s)
        part1 = ''
        part2 = ''
        index = length_s - shift
        while index < length_s:
            part1 += s[index]
            index += 1
        index = 0
        while index < length_s - shift:
            part2 += s[index]
            index += 1
        return part1 + part2