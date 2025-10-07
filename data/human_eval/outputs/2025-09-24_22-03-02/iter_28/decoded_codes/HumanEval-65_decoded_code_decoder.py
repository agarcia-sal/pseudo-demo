def circular_shift(x, shift):
    s = str(x)
    if shift > len(s):
        result = ""
        index = len(s) - 1
        while index >= 0:
            result += s[index]
            index -= 1
        return result
    else:
        length = len(s)
        part1 = ""
        start_index_part1 = length - shift
        index = start_index_part1
        while index < length:
            part1 += s[index]
            index += 1
        part2 = ""
        index = 0
        while index < start_index_part1:
            part2 += s[index]
            index += 1
        return part1 + part2