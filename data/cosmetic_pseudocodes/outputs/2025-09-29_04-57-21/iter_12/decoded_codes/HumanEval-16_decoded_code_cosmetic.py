from typing import Set

def count_distinct_characters(input_string: str) -> int:
    normalized_string: str = ''
    index: int = 0
    while index < len(input_string):
        current_char: str = input_string[index].lower()
        normalized_string += current_char
        index += 1

    unique_chars: Set[str] = set()
    idx: int = 0
    while idx < len(normalized_string):
        char = normalized_string[idx]
        if char not in unique_chars:
            unique_chars.add(char)
        idx += 1

    return len(unique_chars)