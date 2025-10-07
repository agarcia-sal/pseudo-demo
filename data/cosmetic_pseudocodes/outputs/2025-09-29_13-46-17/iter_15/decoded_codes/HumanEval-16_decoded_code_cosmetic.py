from typing import List


def count_distinct_characters(input_string: str) -> int:
    seen_chars: List[str] = []
    index: int = 0
    length: int = len(input_string)
    while index < length:
        char = input_string[index].lower()
        if char not in seen_chars:
            seen_chars.append(char)
        index += 1
    return len(seen_chars)