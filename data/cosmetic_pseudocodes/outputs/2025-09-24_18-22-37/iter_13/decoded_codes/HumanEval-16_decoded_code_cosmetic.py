from typing import Set

def count_distinct_characters(source_text: str) -> int:
    lowered_text: str = source_text.lower()
    temp_chars_set: Set[str] = set()
    idx: int = 0
    text_length: int = len(lowered_text)
    while idx < text_length:
        temp_chars_set.add(lowered_text[idx])
        idx += 1
    result_count: int = len(temp_chars_set)
    return result_count