from typing import Set

def count_distinct_characters(input_string: str) -> int:
    unique_chars: Set[str] = set()
    pos: int = 0
    while pos < len(input_string):
        current_char: str = input_string[pos].lower()
        unique_chars.add(current_char)
        pos += 1
    return len(unique_chars)