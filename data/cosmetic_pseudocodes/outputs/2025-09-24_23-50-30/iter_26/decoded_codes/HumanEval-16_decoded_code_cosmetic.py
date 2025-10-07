from typing import List

def count_distinct_characters(sample_text: str) -> int:
    char_collection: List[str] = []
    for index in range(1, len(sample_text) + 1):
        current_char: str = sample_text[index - 1].lower()
        if current_char not in char_collection:
            char_collection.append(current_char)
    return len(char_collection)