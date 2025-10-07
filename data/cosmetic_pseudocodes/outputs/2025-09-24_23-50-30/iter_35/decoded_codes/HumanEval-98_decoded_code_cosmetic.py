from typing import List

def count_upper(string_input: str) -> int:
    accumulator: int = 0
    positions: List[int] = []
    iterator: int = 0
    while iterator < len(string_input):
        positions.append(iterator)
        iterator += 2

    for element in positions:
        if string_input[element] in ("A", "E", "I", "O", "U"):
            accumulator += 1

    return accumulator