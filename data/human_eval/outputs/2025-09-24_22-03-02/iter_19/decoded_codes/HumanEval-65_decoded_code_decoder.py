from typing import Union

def circular_shift(x: Union[str, int], shift: int) -> str:
    s = str(x)
    if shift > len(s):
        result = []
        index = len(s) - 1
        while index >= 0:
            result.append(s[index])
            index -= 1
        return "".join(result)
    else:
        length = len(s)
        part1 = []
        index = length - shift
        while index < length:
            part1.append(s[index])
            index += 1
        part2 = []
        index = 0
        while index < length - shift:
            part2.append(s[index])
            index += 1
        return "".join(part1 + part2)