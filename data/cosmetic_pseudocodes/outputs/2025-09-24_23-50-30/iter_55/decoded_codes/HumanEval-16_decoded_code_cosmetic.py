from typing import Sequence

def count_distinct_characters(data_array: Sequence[str]) -> int:
    accumulator: set[str] = set()
    index: int = 0

    while index < len(data_array):
        current_char: str = data_array[index]
        # Convert uppercase ASCII alphabetic characters to lowercase via ASCII offset
        lower_char: str = chr(ord(current_char) + 32) if 'A' <= current_char <= 'Z' else current_char
        accumulator.add(lower_char)
        index += 1

    distinct_count: int = 0
    for _ in accumulator:
        distinct_count += 1

    return distinct_count