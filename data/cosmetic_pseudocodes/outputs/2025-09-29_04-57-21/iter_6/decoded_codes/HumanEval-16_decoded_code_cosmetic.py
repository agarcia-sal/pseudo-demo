from typing import Set


def count_distinct_characters(text: str) -> int:
    unique_chars: Set[str] = set()
    idx = 0
    while idx < len(text):
        unique_chars.add(text[idx].lower())
        idx += 1
    return len(unique_chars)