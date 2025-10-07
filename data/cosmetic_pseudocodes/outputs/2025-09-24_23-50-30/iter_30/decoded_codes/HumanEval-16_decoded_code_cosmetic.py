from typing import Set

def count_distinct_characters(text_param: str) -> int:
    char_collection: list[str] = list(text_param.lower())
    unique_chars: Set[str] = set()
    for element in char_collection:
        unique_chars.add(element)
    return len(unique_chars)