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
        part1 = ""
        start_index_part1 = len(s) - shift
        end_index_part1 = len(s) - 1
        index = start_index_part1
        while index <= end_index_part1:
            part1 += s[index]
            index += 1
        part2 = ""
        start_index_part2 = 0
        end_index_part2 = len(s) - shift - 1
        index = start_index_part2
        while index <= end_index_part2:
            part2 += s[index]
            index += 1
        return part1 + part2