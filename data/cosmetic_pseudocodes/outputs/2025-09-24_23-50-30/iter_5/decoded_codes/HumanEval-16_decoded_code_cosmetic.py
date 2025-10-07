from typing import Set


def count_distinct_characters(text: str) -> int:
    characters_set: Set[str] = set()
    index: int = 0

    while index < len(text):
        current_char: str = text[index].lower()
        if current_char not in characters_set:
            characters_set.add(current_char)
        index += 1

    return len(characters_set)