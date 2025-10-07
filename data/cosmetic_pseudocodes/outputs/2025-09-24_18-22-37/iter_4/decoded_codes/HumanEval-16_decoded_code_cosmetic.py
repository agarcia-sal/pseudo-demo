from typing import Set

def count_distinct_characters(text: str) -> int:
    unique_chars: Set[str] = set()
    index: int = 1
    while index <= len(text):
        unique_chars.add(text[index - 1].lower())  # 1-based indexing in pseudocode translated to 0-based in Python
        index += 1
    return len(unique_chars)