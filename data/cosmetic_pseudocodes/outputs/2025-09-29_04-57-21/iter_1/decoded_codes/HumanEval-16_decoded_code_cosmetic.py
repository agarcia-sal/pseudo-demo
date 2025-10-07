from typing import Set

def count_distinct_characters(input_string: str) -> int:
    unique_chars: Set[str] = set()
    for character in input_string.lower():
        unique_chars.add(character)
    return len(unique_chars)