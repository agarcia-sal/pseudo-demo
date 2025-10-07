from typing import Set


def count_distinct_characters(source_text: str) -> int:
    temp_collection: Set[str] = set()
    idx: int = 1
    while idx <= len(source_text):
        char_candidate = source_text[idx - 1].lower()  # Adjust for 0-based indexing
        if char_candidate not in temp_collection:
            temp_collection.add(char_candidate)
        idx += 1
    return len(temp_collection)