from typing import Sequence

def count_distinct_characters(text_sequence: Sequence[str]) -> int:
    temp_set: set[str] = set()
    index: int = 0
    length: int = len(text_sequence)
    while index < length:
        current_char: str = text_sequence[index].lower()
        temp_set.add(current_char)
        index += 1
    return len(temp_set)