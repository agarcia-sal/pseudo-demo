from typing import Set

def count_distinct_characters(input_string: str) -> int:
    lowered_string: str = ""
    unique_chars: Set[str] = set()
    idx: int = 0

    while idx < len(input_string):
        lowered_string += input_string[idx].lower()
        idx += 1

    idx = 0
    while idx < len(lowered_string):
        unique_chars.add(lowered_string[idx])
        idx += 1

    return len(unique_chars)