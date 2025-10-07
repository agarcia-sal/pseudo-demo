from typing import List


def count_distinct_characters(input_string: str) -> int:
    temp_str: str = input_string.lower()
    char_collection: List[str] = [ch for ch in temp_str]
    unique_chars: List[str] = []
    for element in char_collection:
        if element not in unique_chars:
            unique_chars.append(element)
    result: int = len(unique_chars)
    return result