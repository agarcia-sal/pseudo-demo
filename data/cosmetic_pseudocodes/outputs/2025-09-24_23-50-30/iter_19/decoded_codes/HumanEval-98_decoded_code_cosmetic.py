from typing import List


def count_upper(string_input: str) -> int:
    accumulator: int = 0
    positions: List[int] = []
    cursor: int = 0
    while cursor < len(string_input):
        positions.append(cursor)
        cursor += 2
    for point in positions:
        if string_input[point] in "AEIOU":
            accumulator += 1
    return accumulator