from typing import Union

def circular_shift(x: Union[str, int], shift: int) -> str:
    s = str(x)
    if shift > len(s):
        reversed_string = []
        index = len(s) - 1
        while index >= 0:
            reversed_string.append(s[index])
            index -= 1
        result = ''
        i = 0
        while i < len(reversed_string):
            result += reversed_string[i]
            i += 1
        return result
    else:
        length = len(s)
        part1 = []
        start_index_part1 = length - shift
        index_part1 = start_index_part1
        while index_part1 < length:
            part1.append(s[index_part1])
            index_part1 += 1
        part2 = []
        index_part2 = 0
        while index_part2 < start_index_part1:
            part2.append(s[index_part2])
            index_part2 += 1
        result = ''
        i = 0
        while i < len(part1):
            result += part1[i]
            i += 1
        j = 0
        while j < len(part2):
            result += part2[j]
            j += 1
        return result