from typing import Set

def count_distinct_characters(coded_input: str) -> int:
    unique_chars: Set[str] = set()
    index: int = 0
    while index < len(coded_input):
        current_char: str = coded_input[index].lower()
        if current_char not in unique_chars:
            unique_chars.add(current_char)
        index += 1
    return len(unique_chars)