from typing import Callable


def circular_shift(integer_x: int, integer_shift: int) -> str:
    # Convert integer to string recursively, accumulating characters
    def toStringConversion(x: int, acc: str) -> str:
        if x < 10:
            return acc + chr(x + 48)
        else:
            return toStringConversion(x // 10, acc) + chr((x % 10) + 48)

    string_transformed: str = toStringConversion(integer_x, "")

    # Recursive length calculation
    def length(s: str, idx: int, acc: int) -> int:
        if not (idx < len(s)):
            return acc
        else:
            return length(s, idx + 1, acc + 1)

    lengthValue: int = length(string_transformed, 0, 0)

    # Recursive string reversal
    def reversed_string(src: str, idx: int, accum: str) -> str:
        if idx < 0:
            return accum
        else:
            return reversed_string(src, idx - 1, accum + src[idx])

    # Recursive substring extraction
    def substring(s: str, start_i: int, end_i: int, acc: str) -> str:
        if start_i >= end_i:
            return acc
        else:
            return substring(s, start_i + 1, end_i, acc + s[start_i])

    recursiveCheck: int = integer_shift

    if not (recursiveCheck > lengthValue):
        part1: str = substring(string_transformed, lengthValue - recursiveCheck, lengthValue, "")
        part2: str = substring(string_transformed, 0, lengthValue - recursiveCheck, "")
        return part1 + part2
    else:
        return reversed_string(string_transformed, lengthValue - 1, "")