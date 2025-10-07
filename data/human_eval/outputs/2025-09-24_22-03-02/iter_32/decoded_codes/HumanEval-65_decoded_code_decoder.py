def circular_shift(x, shift) -> str:
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
        part1_start = length - shift
        part1 = ""
        index_part1 = part1_start
        while index_part1 < length:
            part1 += s[index_part1]
            index_part1 += 1
        part2 = ""
        index_part2 = 0
        while index_part2 < part1_start:
            part2 += s[index_part2]
            index_part2 += 1
        return part1 + part2